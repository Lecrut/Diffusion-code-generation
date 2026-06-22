def contains_true_boolean(bool_sequence):
    if not hasattr(bool_sequence, '__iter__'):
        raise ValueError("Input must be an iterable")
    if not hasattr(bool_sequence, '__len__'):
        check_iterable = list(bool_sequence)
        bool_sequence = check_iterable
    if len(bool_sequence) == 0:
        return False
    for element in bool_sequence:
        if element is True:
            return True
    return False

if __name__ == '__main__':
    test_data = [False, False, False, True, False]
    empty_data = []
    negative_data = [False, False, False]
    
    result_with_true = contains_true_boolean(test_data)
    result_empty = contains_true_boolean(empty_data)
    result_negative = contains_true_boolean(negative_data)
    
    print(result_with_true)
    print(result_empty)
    print(result_negative)