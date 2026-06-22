def is_equal(a, b):
    return a == b

if __name__ == '__main__':
    print(is_equal(5, 5))          # True
    print(is_equal("test", "test"))  # True
    print(is_equal([1, 2], [3, 4]))  # False
    print(is_equal({"a": 1}, {"b": 1}))  # False