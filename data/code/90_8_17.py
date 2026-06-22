def check_condition(*args):
    if not args:
        raise ValueError("At least one boolean argument is required")
    for arg in args:
        if not isinstance(arg, bool):
            raise TypeError("All arguments must be boolean values")
    return True if args[0] else _check_remaining(args[1:])

def _check_remaining(rest):
    if not rest:
        return False
    if rest[0]:
        return True
    return _check_remaining(rest[1:])

if __name__ == '__main__':
    result = check_condition(False, False, True, False)
    print(result)