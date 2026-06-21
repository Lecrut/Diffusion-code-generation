import re

def normalize_string(text):
    words = re.sub(r'\W+', ' ', text).lower().split()
    return words

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test string for normalization."
    normalized_words = normalize_string(sample_string)
    print(normalized_words)