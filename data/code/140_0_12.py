import re

def is_alphanumeric(input_string):
    return bool(re.match(r'^[a-zA-Z0-9]+$', input_string))

if __name__ == '__main__':
    test_strings = ['Hello123', 'World!', 'Python3.8', '123456']
    for string in test_strings:
        print(f"'{string}' is alphanumeric: {is_alphanumeric(string)}")