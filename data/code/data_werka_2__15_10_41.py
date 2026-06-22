def is_equal(a, b):
    return a == b

if __name__ == '__main__':
    value1 = [1, 2, 3]
    value2 = [1, 2, 3]
    value3 = "example"
    value4 = "test"
    print(is_equal(value1, value2))  # True
    print(is_equal(value3, value4))  # False
    print(is_equal(3.14, 3.14))      # True
    print(is_equal({"key": "value"}, {"key": "value"}))  # True