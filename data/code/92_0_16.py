def invert_boolean(value):
    return not value

if __name__ == '__main__':
    test_value = True
    inverted_value = invert_boolean(test_value)
    print(inverted_value)

    another_test_value = False
    another_inverted_value = invert_boolean(another_test_value)
    print(another_inverted_value)