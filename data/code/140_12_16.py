import re

def validate_input(value):
    if isinstance(value, str) and value:
        return bool(re.match(r'^[a-zA-Z0-9]+$', value))
    elif isinstance(value, int) and value > 0:
        return True
    return False

if __name__ == '__main__':
    test_values = ["12345", "abcde", "", "123a", -5]
    for val in test_values:
        print(validate_input(val))