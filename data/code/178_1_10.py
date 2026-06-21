import re

def extract_words(text):
    return re.findall(r'\b[a-zA-Z]+\b', text)

if __name__ == '__main__':
    sample_text = "Hello, world! 123 Python is fun. Let's do it!"
    print(extract_words(sample_text))