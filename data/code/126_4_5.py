def yield_equality_check(a, b):
    if a == b:
        yield True
    else:
        yield False
if __name__ == '__main__':
    print(list(yield_equality_check(1, 1)))
    print(list(yield_equality_check(1, 2)))
    print(list(yield_equality_check("hello", "hello")))
    print(list(yield_equality_check("hello", "world")))
    print(list(yield_equality_check([1, 2], [1, 2])))
    print(list(yield_equality_check([1, 2], [3, 4])))
    print(list(yield_equality_check(None, None)))
    print(list(yield_equality_check(0.0, 0)))