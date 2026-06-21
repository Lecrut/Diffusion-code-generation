import re

def split_string(text):
    WORD_PATTERN = '\\b\\w+\\b'
    return re.findall(WORD_PATTERN, text)
if __name__ == '__main__':
    sample_phrase = '  Hello   world! How are you? '
    print('--- Split String ---')
    result = split_string(sample_phrase)
    print(result)