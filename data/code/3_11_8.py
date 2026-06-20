import string

VOWEL_CHARS = frozenset("aeiouAEIOU")

def strip_vowels(text):
    return "".join([char for char in text if char not in VOWEL_CHARS])

if __name__ == "__main__":
    sample_text = "The Quick Brown Fox Jumps Over The Lazy Dog"
    result = strip_vowels(sample_text)
    print(result)