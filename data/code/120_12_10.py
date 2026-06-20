def are_identical(a, b):
    return a is b or (a == b and (not isinstance(a, (list, dict, set))))
if __name__ == '__main__':
    print(are_identical(1, 1))
    print(are_identical([1], [1]))
    print(are_identical({'a': 1}, {'a': 1}))
    print(are_identical({1, 2}, {2, 1}))