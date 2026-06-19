def are_equal(a, b):
    return a == b

if __name__ == '__main__':
    print(are_equal(42, 42))  # True
    print(are_equal('hello', 'world'))  # False
    print(are_equal([1, 2, 3], [1, 2, 3]))  # True
    print(are_equal({'a': 1}, {'a': 1}))  # True