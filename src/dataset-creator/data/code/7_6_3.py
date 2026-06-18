def check_equality(a, b):
    if a == b:
        yield True
    else:
        yield False
if __name__ == '__main__':
    print(list(check_equality(5, 5)))
    print(list(check_equality(5, 6)))
    print(list(check_equality(3.14, 3.14)))
    print(list(check_equality(10, 20)))