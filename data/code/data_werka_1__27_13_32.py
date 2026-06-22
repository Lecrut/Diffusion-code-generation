def check_inequality(a, b):
    return type(a) is type(b) and a != b
if __name__ == '__main__':
    print(check_inequality(5, 10))
    print(check_inequality(5.0, 10.0))
    print(check_inequality('a', 'b'))
    print(check_inequality('a', 'a'))
    print(check_inequality([1, 2], [3]))
    print(check_inequality((1, 2), (1, 2)))