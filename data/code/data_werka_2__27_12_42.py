def check_inequality(a, b):
    if type(a) != type(b):
        return True
    return a != b
if __name__ == '__main__':
    print(check_inequality(5, 10))
    print(check_inequality(5.0, 10.0))
    print(check_inequality('hello', 'world'))
    print(check_inequality([1, 2], [1, 2]))
    print(check_inequality((1, 2), (1, 2)))
    print(check_inequality({1, 2}, {1, 2}))