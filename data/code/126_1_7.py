def are_values_equal(a, b):
    return a == b

if __name__ == '__main__':
    print(are_values_equal(5, 5))
    print(are_values_equal(3.14, 3.14))
    print(are_values_equal("hello", "hello"))
    print(are_values_equal(True, True))
    print(are_values_equal(None, None))