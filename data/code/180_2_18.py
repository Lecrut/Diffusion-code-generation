import re

def contains_word(text, word):
    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()
    words = cleaned_text.split()
    return word.lower() in words

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test."
    search_word = "test"
    result = contains_word(sample_text, search_word)
    print(f"'{search_word}' in '{sample_text}': {result}")