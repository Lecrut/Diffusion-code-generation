def compare_values(a, b):
    return a == b

if __name__ == '__main__':
    print(compare_values(1, 2))
    print(compare_values("hello", "hello"))
    print(compare_values([1, 2], [1, 2]))
    print(compare_values((1, 2), (1, 2)))
    print(compare_values({1: 2}, {1: 2}))
    print(compare_values(True, True))
    print(compare_values(False, False))
    print(compare_values(None, None))