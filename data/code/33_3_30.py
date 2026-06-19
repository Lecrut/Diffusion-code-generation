import re

def filter_alphanumeric(input_string):
    return ''.join(re.findall(r'[A-Za-z0-9]', input_string))

if __name__ == '__main__':
    sample_input = "Hello, World! 123"
    result = filter_alphanumeric(sample_input)
    print(result)