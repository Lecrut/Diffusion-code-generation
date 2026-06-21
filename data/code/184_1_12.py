import re

def detect_word_boundary(text, pattern):
    regex = re.compile('\\b' + re.escape(pattern) + '\\b')
    return bool(regex.search(text))
if __name__ == '__main__':
    text = 'The quick brown fox jumps over the lazy dog'
    pattern = 'fox'
    print(detect_word_boundary(text, pattern))