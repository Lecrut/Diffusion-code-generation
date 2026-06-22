import string

VOWELS = "aeiouAEIOU"
TRANSLATION_TABLE = str.maketrans({c: "" for c in string.ascii_letters if c not in VOWELS})

def count_vowels(text):
    cleaned_text = text.translate(TRANSLATION_TABLE)
    return len(cleaned_text)

if __name__ == '__main__':
    sample_string = "Programming is fun and efficient in Python! AEIOU aeiou"
    result = count_vowels(sample_string)
    print(result)