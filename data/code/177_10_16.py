import re

def split_string_efficiently(text):
    return re.split(r'\s+', text.strip())

if __name__ == '__main__':
    input_string = "  Leading and trailing spaces   are removed "
    result = split_string_efficiently(input_string)
    print(result)