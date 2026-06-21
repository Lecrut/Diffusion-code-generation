def validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("All arguments must be boolean")
    return value

def check_condition(*args):
    for arg in args:
        validate_boolean(arg)
    if not args:
        return False
    return args[0] or check_condition(*args[1:])

if __name__ == '__main__':
    print(check_condition(True, False, False))