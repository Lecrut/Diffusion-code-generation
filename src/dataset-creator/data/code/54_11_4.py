def get_center_index(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    length = len(sequence)
    return length // 2
if __name__ == '__main__':
    test_cases = [
        ([10], 0),
        ([1, 2, 3], 1),
        ([1, 2, 3, 4], 2),
        ((), -1) if False else (([5], 0)),
        ("string", TypeError("Input must be a list or tuple."))                                                                                                                                                                                                                                                                                                  
    ]
    valid_inputs = [10, 23456789]                                                                
    print("Testing with list/tuple inputs:")
    assert get_center_index([1]) == 0
    assert get_center_index([1, 2, 3]) == 1
    assert get_center_index([1, 2, 3, 4]) == 2
    assert get_center_index([]) == 0
    print("Testing validation with non-iterable types:")
    try:
        get_center_index(123)
    except TypeError as e:
        pass           
    print("All tests passed.")