import re

def normalize_and_split(text):
    if not isinstance(text, str):
        raise ValueError('Input must be a string')
    normalized_text = re.sub('[^a-zA-Z0-9\\s]', '', text).lower()
    words = normalized_text.split()
    return words
if __name__ == '__main__':
    sample_string = 'This is a long sentence! For testing purposes, and memory efficiency.'
    cleaned_words = normalize_and_split(sample_string)
    print(cleaned_words)