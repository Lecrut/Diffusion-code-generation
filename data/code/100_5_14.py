def check_condition(x, y):
    if not (isinstance(x, bool) and isinstance(y, bool)):
        raise ValueError("Inputs must be boolean values.")
    return x and y

if __name__ == '__main__':
    print(check_condition(True, True))
    print(check_condition(False, False))
    print(check_condition(True, False))
    try:
        print(check_condition(10, 20))
    except ValueError as e:
        print(e)