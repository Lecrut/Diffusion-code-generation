import re

def clean_and_split(text):
    if not isinstance(text, str):
        raise ValueError('Input must be a string')
    words = re.findall('\\b\\w+\\b', text)
    return words
if __name__ == '__main__':
    long_text = 'this is a very long sentence! designed to test, the efficiency of word splitting; on extremely long strings& for time & space optimization.'
    words = clean_and_split(long_text)
    print(words)