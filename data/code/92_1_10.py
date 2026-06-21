def find_opposite_truth(flag):
    NEGATE = {True: False, False: True}
    return NEGATE[flag]

if __name__ == '__main__':
    test_input = True
    output = find_opposite_truth(test_input)
    print(output)
    test_input = False
    output = find_opposite_truth(test_input)
    print(output)