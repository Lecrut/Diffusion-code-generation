def check_equality(a, b):
    return a == b

if __name__ == '__main__':
    value1 = 20
    value2 = 20.0
    print(check_equality(value1, value2))
    print(check_equality("hello", "goodbye"))
    print(check_equality([3, 4], [3, 4]))
    print(check_equality(None, None))