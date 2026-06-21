import re

def extract_words(text):
    pattern = r'\b\w+\b'
    return re.findall(pattern, text)

if __name__ == '__main__':
    sample_text = "Hello, this is a test string with multiple words."
    print(extract_words(sample_text))