import re

WORD_PATTERN = r'\b\w+\b'

def extract_words(input_string):
    words = re.findall(WORD_PATTERN, input_string)
    return words

if __name__ == '__main__':
    SAMPLE_INPUT = """Hello, world! This is a test string with multiple words,
    including numbers like 123 and special characters #@$%^&*()."""
    
    extracted_words = extract_words(SAMPLE_INPUT)
    print(extracted_words)