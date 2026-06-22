import string

VOWELS = "aeiouAEIOU"
TRANSLATION_TABLE = str.maketrans("", "", VOWELS)

def strip_vowels(text):
    return text.translate(TRANSLATION_TABLE)

if __name__ == '__main__':
    sample_text = "Hello World! Python is amazing."
    result = strip_vowels(sample_text)
    print(result)