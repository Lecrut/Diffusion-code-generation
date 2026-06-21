import re

def split_by_whitespace(input_string):
    return re.split(r'\s+', input_string)

if __name__ == '__main__':
    sample_string = "Hello   world\tthis is a test"
    print(split_by_whitespace(sample_string))