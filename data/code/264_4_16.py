import re
WORD_PATTERN = '\\b\\w+\\b'

def find_distinct_words(text):
    words = re.findall(WORD_PATTERN, text.lower())
    distinct_words = set(words)
    return distinct_words
if __name__ == '__main__':
    sample_string = 'This is a test string with repeated words and some punctuation.'
    result = find_distinct_words(sample_string)
    print(result)