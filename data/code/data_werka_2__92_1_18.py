TRUE_VALUE = True
FALSE_VALUE = False

def find_opposite_truth(value: bool) -> bool:
    if value is TRUE_VALUE:
        return FALSE_VALUE
    return TRUE_VALUE

if __name__ == '__main__':
    test_input = True
    output = find_opposite_truth(test_input)
    print(output)
    test_input = False
    output = find_opposite_truth(test_input)
    print(output)