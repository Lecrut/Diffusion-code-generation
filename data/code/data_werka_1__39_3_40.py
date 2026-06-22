import re

def extract_words(input_string):
    words = re.findall(r'\b\w+\b', input_string)
    return words

if __name__ == '__main__':
    sample_input = """Hello, world! This is a test string with numbers 123 and symbols #@$.
    New lines are also handled."""
    extracted_words = extract_words(sample_input)
    print(extracted_words)