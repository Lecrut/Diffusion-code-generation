import re
def classify_text_characters(raw_text: str) -> dict:
    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    symbol_count = 0
    alphabetic_count = 0
    whitespace_count = 0
    for char in raw_text:
        if 'a' <= char <= 'z':
            lowercase_count += 1
            alphabetic_count += 1
        elif 'A' <= char <= 'Z':
            uppercase_count += 1
            alphabetic_count += 1
        elif '0' <= char <= '9':
            digit_count += 1
        elif char.isspace():
            whitespace_count += 1
        elif re.match(r'[A-Za-z]', char) or re.match(r'[^A-Za-z0-9\s]', char):
            symbol_count += 1
            alphabetic_count += 1
    total_characters = len(raw_text)
    result = {
        "total_characters": total_characters,
        "lowercase_count": lowercase_count,
        "uppercase_count": uppercase_count,
        "digit_count": digit_count,
        "symbol_count": symbol_count,
        "alphabetic_count": alphabetic_count,
        "whitespace_count": whitespace_count,
    }
    return result
if __name__ == '__main__':
    sample_text = "Hello World! 123 Python is fun."
    print(f"Raw Input: {sample_text}")
    processed_data = classify_text_characters(sample_text)
    print("Processed Result:")
    for key, value in processed_data.items():
        print(f"{key}: {value}")