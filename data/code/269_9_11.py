import re

def extract_punctuation(text):
    return re.findall(r'[^\w\s]', text)

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test string with punctuation:.,;!?()"
    print(extract_punctuation(sample_text))