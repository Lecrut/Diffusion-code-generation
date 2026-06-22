TRUE_SENTINEL = True

def evaluate_boolean_sequence(seq):
    if not seq:
        return False
    for element in seq:
        if element is TRUE_SENTINEL:
            return True
    return False

if __name__ == '__main__':
    test_list = [False, False, True, False]
    computed_result = evaluate_boolean_sequence(test_list)
    print(computed_result)