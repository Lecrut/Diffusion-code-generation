import re
def classify_text_characters(raw_text: str) -> dict:
    vowels = "aeiouAEIOU"
    consonants = "bcdfghJKLMNLPQRSTWHYZ"
    digits = "0123456789"
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    punctuation_count = 0
    other_count = 0
    for char in raw_text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            if char in vowels:
                vowel_count += 1
            elif char in consonants:
                consonant_count += 1
            else:
                other_count += 1
        elif '0' <= char <= '9':
            digit_count += 1
        elif char in punctuation:
            punctuation_count += 1
        else:
            other_count += 1
    total_characters = len(raw_text)
    result = {
        "total_characters": total_characters,
        "vowels": vowel_count,
        "consonants": consonant_count,
        "digits": digit_count,
        "punctuation": punctuation_count,
        "other_characters": other_count,
    }
    return result
if __name__ == '__main__':
    sample_text = "Hello World! 123 abc"
    print(classify_text_characters(sample_text))