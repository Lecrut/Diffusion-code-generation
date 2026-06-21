import re

def extract_words(text):
    return re.findall(r'\b[a-zA-Z]+\b', text)

if __name__ == '__main__':
    sample_text = "Hello, world! 123 Python 456 is fun."
    print(extract_words(sample_text))