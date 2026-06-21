import re

def split_string_efficiently(text):
    return re.split(r'\s+', text)

if __name__ == '__main__':
    input_string = "  This   is a test string with multiple spaces and tabs\t"
    result = split_string_efficiently(input_string)
    print(result)