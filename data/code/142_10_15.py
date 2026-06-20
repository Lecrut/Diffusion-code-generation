def are_booleans_equal(a, b):
    not_a = not a
    not_b = not b
    return not_a == not_b

if __name__ == '__main__':
    print(are_booleans_equal(False, False))
    print(are_booleans_equal(True, True))
    print(are_booleans_equal(True, False))