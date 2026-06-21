import re

def extract_words(text):
    word_pattern = '\\b\\w+\\b'
    words = set()
    for match in re.finditer(word_pattern, text.lower()):
        words.add(match.group())
    return list(words)
if __name__ == '__main__':
    sample_string = 'Hello world! This is a test, world, and hello again.'
    result = extract_words(sample_string)
    print(result)