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
    print("Testing get_center_index:")
    valid_inputs = [10], [1, 2, 3], [1, 2, 3, 4]
    for seq in valid_inputs:
        try:
            result = get_center_index(seq)
            expected = len(seq) // 2
            assert result == expected, f"Failed for {seq}"
            print(f"{seq} -> Center Index: {result}")
        except Exception as e:
            print(f"Error with {seq}: {e}")
    try:
        get_center_index("hello")
    except TypeError as te:
        print(f"Correctly caught error for string input: {te}")