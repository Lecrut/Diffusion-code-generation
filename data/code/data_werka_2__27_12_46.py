def check_inequality(a, b):
    if type(a) != type(b):
        return True
    return a != b
if __name__ == '__main__':
    print(check_inequality(10, 20))
    print(check_inequality('hello', 'world'))
    print(check_inequality(3.5, 3.5))
    print(check_inequality(True, False))
    print(check_inequality([1, 2], [1, 2]))