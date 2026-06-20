import re

def extract_words(text):
    return re.findall(r'[A-Za-z0-9]+', text)

if __name__ == '__main__':
    sample_text = "Hello, world! 123 test_case."
    result = extract_words(sample_text)
    print(result)