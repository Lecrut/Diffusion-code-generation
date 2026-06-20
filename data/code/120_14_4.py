def fast_compare(a, b):
    return a == b

if __name__ == '__main__':
    print(fast_compare(1, 2))
    print(fast_compare("hello", "hello"))
    print(fast_compare([1, 2], [1, 2]))
    print(fast_compare((1, 2), (1, 2)))
    print(fast_compare({1: 2}, {1: 2}))