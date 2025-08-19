import json
import os

input_file = '/Users/pcadabam/Projects/numos1/atob_analysis/atob.json'

print("Reading JSON file...")
original_size = os.path.getsize(input_file)
print(f"Original file size: {original_size / (1024*1024):.2f} MB")

with open(input_file, 'r') as f:
    data = json.load(f)

def remove_screenshots(obj):
    if isinstance(obj, dict):
        if 'screenshot' in obj:
            del obj['screenshot']
        if 'screenshots' in obj:
            del obj['screenshots']
        for key, value in list(obj.items()):
            remove_screenshots(value)
    elif isinstance(obj, list):
        for item in obj:
            remove_screenshots(item)

remove_screenshots(data)

print("Writing cleaned JSON file...")
with open(input_file, 'w') as f:
    json.dump(data, f, indent=2)

new_size = os.path.getsize(input_file)
print(f"New file size: {new_size / (1024*1024):.2f} MB")
print(f"Size reduction: {(original_size - new_size) / (1024*1024):.2f} MB")
print("Screenshot fields removed successfully!")