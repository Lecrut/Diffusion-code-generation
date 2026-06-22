import re

def find_unique_punctuation(text):
    punctuation = set(re.findall(r'[^\w\s]', text))
    return list(punctuation)

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. It has punctuation:.,;:'\"!?()[]{}<>"
    unique_punctuation = find_unique_punctuation(sample_text)
    print(unique_punctuation)