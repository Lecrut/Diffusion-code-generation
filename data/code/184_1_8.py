import re

def detect_word_boundary(text, pattern):
    compiled_pattern = re.compile(r'\b' + re.escape(pattern) + r'\b')
    return bool(compiled_pattern.search(text))

if __name__ == '__main__':
    sample_text = "This is a test string with the word 'example' in it."
    search_pattern = "example"
    print(detect_word_boundary(sample_text, search_pattern))