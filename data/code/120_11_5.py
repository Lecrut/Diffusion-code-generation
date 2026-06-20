def are_equal(a, b):
    return a == b
if __name__ == '__main__':
    print(are_equal(1, 1))
    print(are_equal(1, '1'))
    print(are_equal([1, 2], [1, 2]))
    print(are_equal([1, 2], (1, 2)))