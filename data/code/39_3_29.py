import re

def extract_words(input_string):
    words = re.findall(r'\b\w+\b', input_string)
    return words

if __name__ == '__main__':
    sample_input = """Hello, world! This is a test string with multiple words,
    including numbers like 123 and special characters #@$%^&*()."""
    result = extract_words(sample_input)
    print(result)