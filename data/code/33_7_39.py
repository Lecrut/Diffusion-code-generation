import re

def remove_all_spaces(input_string):
    return re.sub('\\s+', '', input_string)
if __name__ == '__main__':
    sample_input = 'Here is another\texample with\nmultiple spaces.'
    result = remove_all_spaces(sample_input)
    print(result)