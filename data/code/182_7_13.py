import re

def separate_characters(input_string):
    return re.findall(r'\S', input_string)

if __name__ == '__main__':
    sample_string = "Hello123World!"
    result = separate_characters(sample_string)
    print(result)