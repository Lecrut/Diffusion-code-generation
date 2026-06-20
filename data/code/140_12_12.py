def is_valid_input(value):
    if isinstance(value, str) and value:
        return bool(re.match('^[a-zA-Z0-9]+$', value))
    elif isinstance(value, int) and value > 0:
        return True
    return False
if __name__ == '__main__':
    print(is_valid_input('Hello123'))
    print(is_valid_input(42))
    print(is_valid_input(''))
    print(is_valid_input('Hello!'))
    print(is_valid_input(-5))