def check_equality(a, b):
    if not isinstance(a, (type(None), int, float, str)) or not isinstance(b, (type(None), int, float, str)):
        raise ValueError("Both inputs must be None, int, float, or str")
    return a == b

if __name__ == '__main__':
    print(check_equality(5, 5))
    print(check_equality(10, 5))
    print(check_equality("hello", "hello"))
    print(check_equality(10.5, 10.5))
    print(check_equality(10, 10.0))