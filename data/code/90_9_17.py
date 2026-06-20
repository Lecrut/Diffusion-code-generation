def check_condition(*args):
    if not all(isinstance(arg, bool) for arg in args):
        raise ValueError("All arguments must be boolean values")
    return any(args)

if __name__ == '__main__':
    print(check_condition(True, False, False))
    print(check_condition(False, False, True))
    print(check_condition(False, False, False))