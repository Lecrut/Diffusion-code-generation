import re

def is_alphanumeric(input_string):
    pattern = '^[a-zA-Z0-9]+$'
    return bool(re.match(pattern, input_string))
if __name__ == '__main__':
    print(is_alphanumeric('Hello123'))
    print(is_alphanumeric('Hello World'))
    print(is_alphanumeric('123456'))
    print(is_alphanumeric('!@#$%^&*()'))