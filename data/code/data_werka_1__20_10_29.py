def are_equal(x, y):
    return x == y
if __name__ == '__main__':
    print(are_equal(42, 42))
    print(are_equal('hello', 'world'))
    print(are_equal([1, 2, 3], [1, 2, 3]))
    print(are_equal({'a': 1}, {'a': 2}))