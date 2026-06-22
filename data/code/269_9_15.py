import re

def extract_punctuation(s):
    return re.findall(r'[^\w\s]', s)

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with punctuation:.,;!?()"
    print(extract_punctuation(sample_string))