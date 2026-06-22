import re

def isolate_punctuation(input_string):
    isolated_string = ''
    for char in input_string:
        if char in '!@#$%^&*()_+-=[]{}|;:,.<>?':
            isolated_string += ' ' + char + ' '
        else:
            isolated_string += char
    return isolated_string

if __name__ == '__main__':
    sample_input = "Hello, world! How are you?"
    result = isolate_punctuation(sample_input)
    print(result)