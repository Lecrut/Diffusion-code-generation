import re

def extract_words(text):
    words = re.sub(r'\W+', ' ', text).split()
    return words

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test."
    print(extract_words(sample_text))