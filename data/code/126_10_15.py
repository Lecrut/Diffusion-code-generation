def check_equality(a, b):
    if a is None and b is None:
        return True
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a == b
    if isinstance(a, str) and isinstance(b, str):
        return a == b
    raise ValueError("Unsupported types for equality check")

if __name__ == '__main__':
    print(check_equality(5, 5))
    print(check_equality(10, 5))
    print(check_equality("hello", "hello"))
    print(check_equality(10.5, 10.5))
    try:
        print(check_equality(10, 10.0))
    except ValueError as e:
        print(e)