import re

def remove_spaces(input_string):
    return re.sub('\\s+', '', input_string)
if __name__ == '__main__':
    sample_string = 'This is a test string with multiple   spaces.'
    result = remove_spaces(sample_string)
    print(result)