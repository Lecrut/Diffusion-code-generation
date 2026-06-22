def is_equal(a, b):
    return a == b

if __name__ == '__main__':
    print(is_equal(10, 10))          # True
    print(is_equal("hello", "world"))  # False
    print(is_equal([1, 2, 3], [1, 2, 3]))  # True
    print(is_equal({"a": 1}, {"b": 1}))  # False