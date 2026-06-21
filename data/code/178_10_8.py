import re

def extract_words(text):
    return re.findall(r'\b\w+\b', text.lower())

if __name__ == '__main__':
    sample_string = "Hello world! This is a test, how are you doing today? Python programming is fun."
    extracted = extract_words(sample_string)
    print(extracted)