import re

def strip_spaces(input_string):
    return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    test_input = "Python 3.8 is great!"
    processed_output = strip_spaces(test_input)
    print(processed_output)