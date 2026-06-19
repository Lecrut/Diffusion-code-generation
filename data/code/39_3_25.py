import re

def extract_words(input_string):
    word_pattern = '\\b\\w+\\b'
    words = re.findall(word_pattern, input_string)
    return words
if __name__ == '__main__':
    sample_input = 'Hello, world! This is a test string with multiple words,\n    including numbers like 123 and special characters #@$%^&*().'
    extracted_words = extract_words(sample_input)
    print(extracted_words)