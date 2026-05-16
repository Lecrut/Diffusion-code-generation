def check_equality(a, b):
    return a == b
if __name__ == '__main__':
    print(check_equality(10, 10))
    print(check_equality(10, 11))
    print(check_equality(3.14, 3.1400000000000004))
    print(check_equality("hello", "hello"))
    print(check_equality("hello", "world"))
    print(check_equality(True, 1))