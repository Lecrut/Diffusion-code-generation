import re

def is_alphanumeric(input_string):
    pattern = r'^[a-zA-Z0-9]+$'
    return bool(re.match(pattern, input_string))

if __name__ == '__main__':
    test_strings = ["Hello123", "World!", "Python3.8", "123456"]
    for string in test_strings:
        print(f"'{string}' is alphanumeric: {is_alphanumeric(string)}")