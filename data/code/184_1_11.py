import re

def detect_word_boundary(text):
    pattern = r'\bword\b'
    compiled_pattern = re.compile(pattern)
    return bool(compiled_pattern.search(text))

if __name__ == '__main__':
    sample_text = "This is a test string with the word 'word' in it."
    print(detect_word_boundary(sample_text))