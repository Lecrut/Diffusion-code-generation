def are_values_equal(a, b):
    return a == b
if __name__ == '__main__':
    print(are_values_equal(1, 1))
    print(are_values_equal(5, 5))
    print(are_values_equal(1, 2))
    print(are_values_equal('a', 'a'))
    print(are_values_equal('a', 'b'))
    print(are_values_equal(True, True))
    print(are_values_equal(True, False))