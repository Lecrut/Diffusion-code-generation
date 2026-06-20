import re

def is_alphanumeric(input_string):
    return bool(re.match('^[a-zA-Z0-9]+$', input_string))
if __name__ == '__main__':
    print(is_alphanumeric('Hello123'))
    print(is_alphanumeric('Hello 123'))