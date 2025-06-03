import json

input_path = 'lyrics.json'
output_path = 'cleaned_lyrics.json'

def clean_element(elem):
    # If element is a dict and has key, singer, or songPart — clear it
    if isinstance(elem, dict):
        if any(k in elem for k in ("key", "singer", "songPart")):
            return {}
    return elem

# Load the file
with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Process each lyric entry
for item in data.get("lyrics", []):
    if "element" in item:
        item["element"] = clean_element(item["element"])

# Save cleaned output
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Done! Output saved to cleaned_lyrics.json")
