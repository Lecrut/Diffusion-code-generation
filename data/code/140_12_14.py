def validate_input(value):
    if isinstance(value, str) and value:
        return bool(re.match('^[a-zA-Z0-9]+$', value))
    elif isinstance(value, int) and value > 0:
        return True
    raise ValueError("Input must be a non-empty string with alphanumeric characters or a positive integer")

if __name__ == '__main__':
    print(validate_input('Hello123'))
    print(validate_input(42))
    try:
        print(validate_input(''))
    except ValueError as e:
        print(e)
    try:
        print(validate_input('Hello!'))
    except ValueError as e:
        print(e)
    try:
        print(validate_input(-5))
    except ValueError as e:
        print(e)