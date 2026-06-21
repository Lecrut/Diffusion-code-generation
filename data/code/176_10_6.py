import re
WORD_PATTERN = '\\b\\w+\\b'

def extract_words(text):
    return re.findall(WORD_PATTERN, text)
if __name__ == '__main__':
    sample_text = 'This is a test string with words, including multiple sentences!'
    print(extract_words(sample_text))