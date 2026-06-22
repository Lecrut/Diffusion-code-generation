import re

def remove_spaces(input_string):
    return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    sample_string = "  Leading and trailing spaces  "
    result = remove_spaces(sample_string)
    print(result)