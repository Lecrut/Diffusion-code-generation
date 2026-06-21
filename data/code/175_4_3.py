import re

def find_words(text):
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_text = "Hello, this is a test string with multiple words."
    print(find_words(sample_text))