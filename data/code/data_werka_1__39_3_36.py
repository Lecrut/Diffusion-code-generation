import re

def extract_words(input_string):
    word_pattern = '\\b\\w+\\b'
    words = re.findall(word_pattern, input_string)
    return words
if __name__ == '__main__':
    sample_input = "Hello, World! This is a test.\n    It should extract words like 'Hello', 'World', and so on."
    extracted_words = extract_words(sample_input)
    print(extracted_words)