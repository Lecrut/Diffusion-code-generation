TRUE_FLAG = True

def has_true_element(boolean_sequence):
    for item in boolean_sequence:
        if item is TRUE_FLAG:
            return True
    return False

if __name__ == '__main__':
    test_values = [False, False, True, False]
    result = has_true_element(test_values)
    print(result)