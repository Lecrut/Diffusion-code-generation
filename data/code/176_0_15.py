import re

def extract_words(text):
    words = set()
    for word in re.findall(r'\b\w+\b', text.lower()):
        words.add(word)
    return list(words)

if __name__ == '__main__':
    sample_string = "Hello world! This is a test, world, and hello again."
    result = extract_words(sample_string)
    print(result)