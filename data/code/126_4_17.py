def check_equality(a, b):
    if type(a) != type(b):
        return False
    return a == b
if __name__ == '__main__':
    print(check_equality(10, 10))
    print(check_equality(10, 20))
    print(check_equality('hello', 'hello'))
    print(check_equality('hello', 'world'))
    print(check_equality([1, 2], [1, 2]))
    print(check_equality([1, 2], [1, 3]))