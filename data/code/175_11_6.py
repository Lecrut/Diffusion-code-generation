import re

def clean_and_split(text):
    words = re.findall(r'\b\w+\b', text)
    return words

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. 123."
    result = clean_and_split(sample_text)
    print(result)