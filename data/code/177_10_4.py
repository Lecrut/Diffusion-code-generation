import re

def split_by_whitespace(input_string):
    return re.split(r'\s+', input_string)

if __name__ == '__main__':
    sample = "This is  a   test string"
    print(split_by_whitespace(sample))