import re

def remove_whitespace(s):
    return re.sub(r'\s+', '', s)

if __name__ == '__main__':
    sample_string = "  This is a \t test string with \n various whitespace.  "
    cleaned_string = remove_whitespace(sample_string)
    print(cleaned_string)