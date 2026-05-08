def check_equality(a, b):
    return a == b
if __name__ == '__main__':
    print(check_equality(10, 10))
    print(check_equality(10.0, 10))
    print(check_equality(10, 10.0))
    print(check_equality("hello", "hello"))
    print(check_equality("hello", "world"))
    print(check_equality(3.14, 3.1400000000000001))
    print(check_equality([1], [1]))
    print(check_equality(None, None))