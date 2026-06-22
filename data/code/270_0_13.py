import re

def remove_spaces(input_string):
    return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    sample = "Hello, World! This is a test."
    print(remove_spaces(sample))