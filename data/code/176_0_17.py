import re
WORD_PATTERN = '\\b\\w+\\b'

def extract_words(text):
    lower_text = text.lower()
    words = re.findall(WORD_PATTERN, lower_text)
    return list(set(words))
if __name__ == '__main__':
    sample_string = 'Hello world! This is a test, world, and hello again.'
    result = extract_words(sample_string)
    print(result)