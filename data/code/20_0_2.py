def are_equal(item1, item2):
    return item1 == item2
if __name__ == '__main__':
    print(are_equal(1, 1))
    print(are_equal(1.0, 1))
    print(are_equal("hello", "hello"))
    print(are_equal(3.14, 3.1400000000000004))
    print(are_equal([1, 2], [1, 2]))
    print(are_equal(None, None))
    print(are_equal(5, 6))
    print(are_equal("a", "b"))
    print(are_equal(True, 1))