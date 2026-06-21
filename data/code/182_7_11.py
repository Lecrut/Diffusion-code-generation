import re

def split_string_to_chars(input_string):
    return list(re.findall(r'\S', input_string))

if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = split_string_to_chars(sample_string)
    print(result)