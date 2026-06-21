import re

def detect_word_boundary(text):
    pattern = '\\bword\\b'
    compiled_pattern = re.compile(pattern)
    return compiled_pattern.search(text) is not None
if __name__ == '__main__':
    sample_text = "This is a test string with the word 'word' in it."
    print(detect_word_boundary(sample_text))