import re
from collections import defaultdict
def classify_text_characters(raw_text: str) -> dict:
    character_counts = defaultdict(int)
    for char in raw_text:
        if 'a' <= char <= 'z':
            character_counts[char] += 1
        elif 'A' <= char <= 'Z':
            character_counts[char.lower()] += 1
        elif '0' <= char <= '9':
            character_counts[char] += 1
        elif char.isspace():
            character_counts[' '] += 1
        else:
            character_counts['other'] += 1
    return dict(character_counts)
if __name__ == '__main__':
    sample_text = "Hello World! 123, this is a test sentence."
    print(f"Raw Input: {sample_text}\n")
    structured_result = classify_text_characters(sample_text)
    import json
    print("Structured Output:")
    print(json.dumps(structured_result, indent=4))