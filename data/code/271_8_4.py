import re
def classify_text_chars(raw_text: str) -> dict:
    char_counts = {}
    for char in raw_text:
        if 'a' <= char <= 'z':
            char_type = 'lowercase'
        elif 'A' <= char <= 'Z':
            char_type = 'uppercase'
        elif '0' <= char <= '9':
            char_type = 'digit'
        elif ' ' == char:
            char_type = 'space'
        else:
            char_type = 'other'
        if char_type not in char_counts:
            char_counts[char_type] = 0
        char_counts[char_type] += 1
    return char_counts
if __name__ == '__main__':
    sample_text = "Hello World 123! This is a test."
    print(f"Raw Input: {sample_text}")
    structured_result = classify_text_chars(sample_text)
    import json
    print("\nStructured Output:")
    print(json.dumps(structured_result, indent=4))