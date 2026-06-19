import re

def extract_words(input_string):
    words = []
    for line in input_string.splitlines():
        words.extend(re.findall(r'\b\w+\b', line))
    return words

if __name__ == '__main__':
    sample_input = """Hello, world! This is a test string with multiple words,
    including numbers like 123 and special characters #@$%^&*()."""
    extracted_words = extract_words(sample_input)
    print(extracted_words)