import re

def remove_whitespace(input_string):
    return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    sample_string = "  Hello   World! \n This is a\ttest. "
    result = remove_whitespace(sample_string)
    print(result)