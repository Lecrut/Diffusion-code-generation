import re
def classify_characters(text):
    vowels = re.compile(r'[aeiouAEIOU]')
    consonants = re.compile(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]')
    digits = re.compile(r'\d')
    punctuation = re.compile(r'[!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~]')
    vowel_count = len(vowels.findall(text))
    consonant_count = len(consonants.findall(text))
    digit_count = len(digits.findall(text))
    punctuation_count = len(punctuation.findall(text))
    return {
        "vowels": vowel_count,
        "consonants": consonant_count,
        "digits": digit_count,
        "punctuation": punctuation_count
    }
if __name__ == '__main__':
    sample_text = "Hello World 123! This is a test string."
    results = classify_characters(sample_text)
    print(results)