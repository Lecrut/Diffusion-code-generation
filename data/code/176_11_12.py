import re

def find_words(text):
    WORD_PATTERN = r'\b\w+\b'
    return re.findall(WORD_PATTERN, text)

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. Multiple   spaces and punctuation... should work."
    words = find_words(sample_text)
    print(words)