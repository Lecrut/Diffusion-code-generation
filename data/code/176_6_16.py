import re

def normalize_string(input_string):
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
    words = cleaned.lower().split()
    return words

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test string with special characters: @#$%^&*()"
    result = normalize_string(sample_string)
    print(result)