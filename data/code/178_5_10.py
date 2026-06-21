import re

def extract_words(text):
    words = re.findall(r'\b[a-z]+\b', text.lower())
    return words

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test."
    print(extract_words(sample_text))