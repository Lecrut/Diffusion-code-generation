import re

def extract_words(text):
    return re.findall(r'\b[a-zA-Z]+\b', text)

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test string with 123 numbers and $%^&*() characters."
    print(extract_words(sample_text))