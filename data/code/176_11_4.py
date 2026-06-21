import re

def find_words(text):
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test. 123."
    print(find_words(sample_text))