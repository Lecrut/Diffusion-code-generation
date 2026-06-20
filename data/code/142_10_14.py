def are_booleans_equal(a, b):
    TRUE = True
    FALSE = False
    return (not a) == (not b)

if __name__ == '__main__':
    print(are_booleans_equal(True, True))
    print(are_booleans_equal(False, False))
    print(are_booleans_equal(True, False))