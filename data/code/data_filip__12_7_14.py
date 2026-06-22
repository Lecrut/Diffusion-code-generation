import re
import string

def clean_and_verify_integers(input_string: str) -> bool:
    translation_map = str.maketrans('', '', string.punctuation + string.whitespace)
    cleaned_string = input_string.translate(translation_map)
    if not cleaned_string:
        return False
    return cleaned_string.isdigit() or (cleaned_string.startswith('-') and cleaned_string[1:].isdigit() and len(cleaned_string) > 1)

if __name__ == '__main__':
    sample_values = ["123, 456!", "789-0", "abc123", "  42  ", "-99"]
    for value in sample_values:
        result = clean_and_verify_integers(value)
        print(f"Input: '{value}', Is Valid Integer String: {result}")