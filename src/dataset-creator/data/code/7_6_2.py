def check_equality_generator(a, b):
    if a == b:
        yield True
    else:
        yield False
if __name__ == '__main__':
    print(list(check_equality_generator(5, 5)))
    print(list(check_equality_generator(10, 2)))
    print(list(check_equality_generator(3.14, 3.14)))
    print(list(check_equality_generator(1, 0)))