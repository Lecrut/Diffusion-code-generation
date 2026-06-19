import re

def minify_text(input_string):
    return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    sample_input = "  This is a   test string with \t various   spaces and\n new lines. "
    result = minify_text(sample_input)
    print(result)