import re

def validate_input(value):
    if isinstance(value, int) and value > 0:
        return True
    elif isinstance(value, str) and len(value) > 0 and re.match('^[a-zA-Z0-9]+$', value):
        return True
    else:
        return False
if __name__ == '__main__':
    print(validate_input('Hello123'))
    print(validate_input(42))
    print(validate_input(''))
    print(validate_input('Hello!'))
    print(validate_input(-5))