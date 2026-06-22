import re

def strip_spaces(input_str):
    return re.sub(r'\s+', '', input_str)

if __name__ == '__main__':
    sample_text = "This is a test string with spaces."
    result = strip_spaces(sample_text)
    print(result)