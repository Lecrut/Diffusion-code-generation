import re

def extract_words(text):
    return re.sub(r'\W+', ' ', text).split()

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test."
    print(extract_words(sample_text))