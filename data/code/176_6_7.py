import re

def normalize_string(s):
    words = re.findall(r'\b\w+\b', s.lower())
    return words

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test."
    normalized_words = normalize_string(sample_string)
    print(normalized_words)