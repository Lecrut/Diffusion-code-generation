import re
ALPHANUMERIC_PATTERN = '^[a-zA-Z0-9]+$'
POSITIVE_INTEGER_TYPE = int

def validate_input(value):
    if isinstance(value, str) and re.match(ALPHANUMERIC_PATTERN, value):
        return True
    elif isinstance(value, POSITIVE_INTEGER_TYPE) and value > 0:
        return True
    return False
if __name__ == '__main__':
    print(validate_input('Hello123'))
    print(validate_input(42))
    print(validate_input(''))
    print(validate_input('Hello!'))
    print(validate_input(-5))