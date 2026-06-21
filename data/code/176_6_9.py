import re

def normalize_and_split(text):
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    words = cleaned_text.lower().split()
    return words

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test string with special characters: @#$%^&*()_+"
    normalized_words = normalize_and_split(sample_string)
    print(normalized_words)