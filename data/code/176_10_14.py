import re

def extract_words(text):
    WORD_PATTERN = r'\b\w+\b'
    return re.findall(WORD_PATTERN, text)

if __name__ == '__main__':
    sample_text = "This is a test string with words, including multiple sentences!"
    print(extract_words(sample_text))