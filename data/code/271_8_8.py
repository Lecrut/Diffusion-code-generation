import re
def classify_text_characters(raw_text: str) -> dict:
    vowels = "aeiouAEIOU"
    consonants = "bcdfghJKLMNLPQRSTWHYZ"
    other_letters = "".join(c for c in raw_text if c.isalpha() and c not in vowels and c not in consonants)
    digits = "".join(c for c in raw_text if c.isdigit())
    symbols = "".join(c for c in raw_text if not c.isalnum())
    vowel_count = sum(1 for char in raw_text if char in vowels)
    consonant_count = sum(1 for char in raw_text if char in consonants)
    digit_count = len(digits)
    symbol_count = len(symbols)
    letter_count = sum(1 for char in raw_text if char.isalpha())
    result = {
        "raw_text": raw_text,
        "vowel_count": vowel_count,
        "consonant_count": consonant_count,
        "digit_count": digit_count,
        "symbol_count": symbol_count,
        "letter_count": letter_count,
        "other_letters_count": len(other_letters),
    }
    return result
if __name__ == '__main__':
    sample_text = "Hello World! 123 abc@xyz"
    processed_data = classify_text_characters(sample_text)
    print(processed_data)