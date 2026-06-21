import re

def detect_word_boundary(text, pattern):
    regex = re.compile(r'\b' + re.escape(pattern) + r'\b')
    return bool(regex.search(text))

if __name__ == '__main__':
    text = "This is a test string with the word 'example' in it."
    pattern = "example"
    result = detect_word_boundary(text, pattern)
    print(result)