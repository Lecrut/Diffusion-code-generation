import re

def extract_words(text):
    word_boundaries = re.finditer(r'\b\w+\b', text)
    words = [match.group() for match in word_boundaries]
    return words

if __name__ == '__main__':
    sample_text = "Hello, this is a test string with multiple words."
    extracted_words = extract_words(sample_text)
    print(extracted_words)