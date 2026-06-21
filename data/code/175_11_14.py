import re

def clean_string_to_words(input_string):
    words = re.findall(r'\b\w+\b', input_string)
    return words

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test."
    result = clean_string_to_words(sample_string)
    print(result)