import re

def filter_alphanumeric(input_string):
    return ''.join(re.findall(r'\w', input_string))

if __name__ == '__main__':
    sample_input = "Hello, World! 123."
    filtered_output = filter_alphanumeric(sample_input)
    print(filtered_output)