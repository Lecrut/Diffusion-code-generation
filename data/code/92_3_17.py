def invert_booleans(boolean_list):
    return [not x for x in boolean_list]

if __name__ == '__main__':
    test_values = [True, False, True, False]
    inverted_test_values = invert_booleans(test_values)
    print(inverted_test_values)