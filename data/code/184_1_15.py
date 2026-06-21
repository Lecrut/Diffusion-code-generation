import re

def find_word_boundary(text, pattern):
    compiled_pattern = re.compile(r'\b' + re.escape(pattern) + r'\b')
    return bool(compiled_pattern.search(text))

if __name__ == '__main__':
    text = "This is a test string with the word 'example' in it."
    pattern = "example"
    result = find_word_boundary(text, pattern)
    print(result)