import re

def detect_word_boundary(text, pattern):
    regex = re.compile('\\b' + re.escape(pattern) + '\\b')
    return bool(regex.search(text))
if __name__ == '__main__':
    text = "This is a test string with the word 'example' in it."
    pattern = 'example'
    print(detect_word_boundary(text, pattern))