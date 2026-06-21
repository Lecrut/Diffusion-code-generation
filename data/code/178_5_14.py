import re

ALPHABETIC = 'abcdefghijklmnopqrstuvwxyz'

def extract_words(text):
    words = text.split()
    cleaned_words = []
    for word in words:
        cleaned_word = ''.join(filter(lambda char: char.isalnum(), word)).lower()
        if cleaned_word and all(char in ALPHABETIC for char in cleaned_word):
            cleaned_words.append(cleaned_word)
    return cleaned_words

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with some - punctuation and numbers 123."
    words = extract_words(sample_string)
    print(words)