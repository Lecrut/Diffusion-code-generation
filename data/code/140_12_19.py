import re

def validate_input(input_value):
    if isinstance(input_value, str) and input_value:
        return bool(re.match('^[a-zA-Z0-9]+$', input_value))
    elif isinstance(input_value, int) and input_value > 0:
        return True
    return False
if __name__ == '__main__':
    print(validate_input('12345'))
    print(validate_input('abcde'))
    print(validate_input(''))
    print(validate_input(0))
    print(validate_input(-5))
    print(validate_input('abc!@#'))