def check_equality(a, b):
    return a == b
if __name__ == '__main__':
    print(check_equality(5, 5))
    print(check_equality(5, '5'))
    print(check_equality([1, 2], [1, 2]))
    print(check_equality(None, None))