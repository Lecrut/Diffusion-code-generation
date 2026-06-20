def invert_boolean(value):
    return value ^ True

if __name__ == '__main__':
    test_values = [True, False]
    for val in test_values:
        print(invert_boolean(val))