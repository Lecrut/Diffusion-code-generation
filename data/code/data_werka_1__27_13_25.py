def check_inequality(a, b):
    return type(a) is not type(b) or a != b
if __name__ == '__main__':
    print(check_inequality(5, 10))
    print(check_inequality(5.0, 10))
    print(check_inequality('5', '10'))
    print(check_inequality('5', 5))
    print(check_inequality(True, False))
    print(check_inequality(5, 5.0))
    print(check_inequality(5, '5'))
    print(check_inequality([1, 2], [1, 2]))
    print(check_inequality({'a': 1}, {'a': 1}))