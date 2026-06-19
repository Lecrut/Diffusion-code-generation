import re

def remove_whitespace(input_string):
    return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    sample_input = "  This is a   test string with \t various whitespace characters.  "
    result = remove_whitespace(sample_input)
    print(result)