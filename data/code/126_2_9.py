def check_equality(value1, value2):
    return value1 == value2

if __name__ == '__main__':
    print(check_equality(10, 10))
    print(check_equality(5.5, 5.5))
    print(check_equality("hello", "hello"))
    print(check_equality(1, 2))
    print(check_equality(True, True))
    print(check_equality(10, 10.0))