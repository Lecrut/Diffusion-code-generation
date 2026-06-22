import re

def remove_spaces(input_string):
    return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    sample_input = "Python programming is fun!"
    processed_string = remove_spaces(sample_input)
    print(processed_string)