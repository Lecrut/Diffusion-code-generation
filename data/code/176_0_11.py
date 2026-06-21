import re

def extract_words(text):
    return set(re.findall(r'\b\w+\b', text.lower()))

if __name__ == '__main__':
    sample_string = "Hello world! This is a test, world, and hello again."
    words = extract_words(sample_string)
    print(words)