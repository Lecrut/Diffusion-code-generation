import re

def normalize_string(s):
    words = re.findall(r'\b\w+\b', s.lower())
    return words

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test string with special characters: @#$%^&*()."
    print(normalize_string(sample_string))