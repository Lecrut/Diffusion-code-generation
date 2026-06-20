def check_equality(a, b):
    return a == b

if __name__ == '__main__':
    print(check_equality(None, None))
    print(check_equality(42, 42))
    print(check_equality(3.14, 3.14))
    print(check_equality("hello", "hello"))
    print(check_equality(42, "42"))