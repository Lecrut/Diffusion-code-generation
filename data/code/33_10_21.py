import re

def minify_text(input_string):
    return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    sample_input = "  This is a   test string with irregular spacing.  "
    result = minify_text(sample_input)
    print(result)