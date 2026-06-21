import re

def split_string_by_whitespace(text):
    return re.split(r'\s+', text)

if __name__ == '__main__':
    input_string = "  This   is a test string with multiple spaces    between words "
    result = split_string_by_whitespace(input_string)
    print(result)