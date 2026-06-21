import re

def extract_words(text):
    words = re.findall(r'\b\w+\b', text)
    return [word.lower() for word in words]

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test. How are you doing today? Python programming is fun."
    extracted_words = extract_words(sample_string)
    print(extracted_words)