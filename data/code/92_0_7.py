def invert_truth(value):
    return not value
if __name__ == '__main__':
    test_value1 = True
    inverted_value1 = invert_truth(test_value1)
    print(inverted_value1)
    test_value2 = False
    inverted_value2 = invert_truth(test_value2)
    print(inverted_value2)