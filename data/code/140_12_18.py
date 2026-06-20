import re

def validate_input(value):
    if isinstance(value, str) and value:
        return bool(re.match('^[a-zA-Z0-9]+$', value))
    elif isinstance(value, int) and value > 0:
        return True
    return False
if __name__ == '__main__':
    print(validate_input('abc123'))
    print(validate_input(456))
    print(validate_input(''))
    print(validate_input('abc!'))
    print(validate_input(-789))