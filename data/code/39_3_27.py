import re

def is_valid_word(word):
    return bool(re.match(r'\b\w+\b', word))

def extract_words(input_string):
    words = input_string.split()
    valid_words = [word for word in words if is_valid_word(word)]
    return valid_words

if __name__ == '__main__':
    sample_input = """Hello, world! This is a test string with multiple words,
    including numbers like 123 and special characters #@$%^&*()."""
    extracted_words = extract_words(sample_input)
    print(extracted_words)