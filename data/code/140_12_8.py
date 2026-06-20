import re

def is_valid_input(value):
    if isinstance(value, str) and value:
        return bool(re.match('^[a-zA-Z0-9]+$', value))
    elif isinstance(value, int) and value > 0:
        return True
    return False

if __name__ == '__main__':
    test_values = ['Hello123', 42, '', 'Hello!', -5]
    results = {value: is_valid_input(value) for value in test_values}
    print(results)