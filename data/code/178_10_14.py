import re

def extract_words(text):
    return [word.lower() for word in re.findall(r'\b\w+\b', text)]

if __name__ == '__main__':
    sample_string = "Hello world! This is a test, how are you doing today? Python programming is fun."
    extracted = extract_words(sample_string)
    print(extracted)