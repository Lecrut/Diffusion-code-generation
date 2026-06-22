def check_inequality(a, b):
    return type(a) is not type(b) or a != b
if __name__ == '__main__':
    print(check_inequality(5, 5))
    print(check_inequality(5, '5'))
    print(check_inequality('hello', 'hello'))
    print(check_inequality('hello', 'world'))
    print(check_inequality(3.14, 3.14))
    print(check_inequality(3.14, 3))