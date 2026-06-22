import re

def extract_words(input_string):
    pattern = r'\b\w+\b'
    return re.findall(pattern, input_string)

if __name__ == '__main__':
    sample_input = """Hello, world! This is a test string with multiple words,
    including numbers like 123 and special characters #@$%^&*()."""
    result = extract_words(sample_input)
    print(result)