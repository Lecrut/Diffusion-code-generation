import re

def extract_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return set(words)

if __name__ == '__main__':
    sample_string = "Hello world! This is a test, world, and hello again."
    result = extract_words(sample_string)
    print(result)