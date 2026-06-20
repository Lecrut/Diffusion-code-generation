def are_equal(a, b):
    if type(a) != type(b):
        return False
    return a == b
if __name__ == '__main__':
    print(are_equal(5, 5))
    print(are_equal(5, '5'))
    print(are_equal([1, 2], [1, 2]))
    print(are_equal([1, 2], (1, 2)))