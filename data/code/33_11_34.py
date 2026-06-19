import re

def remove_whitespace(input_string):
    return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    sample_input = "  This is \t a sample string with \n various whitespace.  "
    result = remove_whitespace(sample_input)
    print(result)