import re

def extract_words(text):
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test string with punctuation."
    words = extract_words(sample_text)
    print(words)