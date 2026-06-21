import re

def normalize_string(s):
    s = re.sub(r'\W+', ' ', s).lower()
    return s.split()

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test."
    print(normalize_string(sample_string))