def check_or_condition(a, b):
    if not isinstance(a, bool):
        raise ValueError("a must be a boolean")
    if not isinstance(b, bool):
        raise ValueError("b must be a boolean")
    return int(a) | int(b)

if __name__ == '__main__':
    result = check_or_condition(True, False)
    print(result)