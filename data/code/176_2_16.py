import re

def tokenize_string(text):
    WORD_PATTERN = '\\b\\w+\\b'
    return re.findall(WORD_PATTERN, text)
if __name__ == '__main__':
    sample_string = 'This is a sample string with various words and punctuation! How about this?'
    tokens = tokenize_string(sample_string)
    print(tokens)