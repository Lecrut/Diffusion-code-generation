import re
def classify_text_characters(raw_text: str) -> dict:
    vowels = "aeiouAEIOU"
    consonants = "bcdfghJKLMNLPQRSTWHYZ"
    other_letters = "".join(c for c in raw_text if c.isalpha() and c not in vowels and c not in consonants)
    digits = "".join(c for c in raw_text if c.isdigit())
    symbols = "".join(c for c in raw_text if not c.isalnum())
    char_counts = {
        "vowels": 0,
        "consonants": 0,
        "digits": 0,
        "other_letters": 0,
        "symbols": 0,
        "total_alphanumeric": 0
    }
    for char in raw_text:
        if char in vowels:
            char_counts["vowels"] += 1
        elif char in consonants:
            char_counts["consonants"] += 1
        elif char.isdigit():
            char_counts["digits"] += 1
        elif char.isalpha():
            char_counts["other_letters"] += 1
            char_counts["total_alphanumeric"] += 1
        else:
            char_counts["symbols"] += 1
    char_counts["total_alphanumeric"] = char_counts["vowels"] + char_counts["consonants"] + char_counts["digits"] + char_counts["other_letters"]
    return char_counts
if __name__ == '__main__':
    sample_text = "Hello World 123! This is a test sentence."
    result = classify_text_characters(sample_text)
    print(result)