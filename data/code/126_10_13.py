def check_equality(a, b):
    if a is None and b is None:
        return True
    elif (a is None or b is None):
        return False
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a == b
    elif isinstance(a, str) and isinstance(b, str):
        return a == b
    else:
        raise TypeError("Unsupported types for equality check")

if __name__ == '__main__':
    print(check_equality(5, 5))
    print(check_equality(10, 5))
    print(check_equality("hello", "hello"))
    print(check_equality(10.5, 10.5))
    print(check_equality(10, 10.0))