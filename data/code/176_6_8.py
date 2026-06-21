import re

def normalize_string(s):
    s = re.sub(r'[^a-zA-Z0-9\s]', '', s)
    return [word.lower() for word in s.split()]

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test string with special characters: @#$%^&*()."
    print(normalize_string(sample_string))