import re

def remove_whitespace(input_string):
    return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    sample_string = "  This is a   test string with \t various \n whitespace characters.  "
    result = remove_whitespace(sample_string)
    print(result)