def are_booleans_equal(a, b):
    truth_table = {True: True, False: False}
    return truth_table[a] == truth_table[b]

if __name__ == '__main__':
    print(are_booleans_equal(True, True))
    print(are_booleans_equal(False, False))
    print(are_booleans_equal(True, False))