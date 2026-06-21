import re

def split_string_by_characters(input_string):
    return re.findall(r'\S', input_string)

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    characters = split_string_by_characters(sample_string)
    print(characters)