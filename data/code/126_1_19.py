def are_values_equal(a, b):
    return a == b

if __name__ == '__main__':
    print(are_values_equal(1, 2))
    print(are_values_equal("Hello", "hello"))
    print(are_values_equal(True, False))
    print(are_values_equal(None, None))
    print(are_values_equal([1, 2], [1, 2]))