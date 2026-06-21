import re

def clean_string(text):
    return re.sub('[^a-zA-Z0-9\\s]', '', text).lower()

def normalize_string(text):
    cleaned_text = clean_string(text)
    words = cleaned_text.split()
    return words
if __name__ == '__main__':
    sample_string = 'This is a long string! For testing purposes... and memory efficiency?'
    normalized_words = normalize_string(sample_string)
    print(normalized_words)