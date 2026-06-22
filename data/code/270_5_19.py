import re

def remove_spaces(input_string):
    return re.sub('\\s+', '', input_string)
if __name__ == '__main__':
    sample_string1 = 'hello world'
    sample_string2 = '  multiple spaces here  '
    sample_string3 = 'singleword'
    print(remove_spaces(sample_string1))
    print(remove_spaces(sample_string2))
    print(remove_spaces(sample_string3))