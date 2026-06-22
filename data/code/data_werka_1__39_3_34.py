import re

def extract_words(input_string):
    words = re.findall(r'\b\w+\b', input_string)
    return words

if __name__ == '__main__':
    sample_input = """
    This is a sample input string with several words,
    including numbers like 123 and special characters #@$%^&*().
    """
    extracted_words = extract_words(sample_input)
    print(extracted_words)