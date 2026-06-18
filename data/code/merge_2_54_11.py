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
        ((), -1),
        ("invalid", TypeError)
    ]
    for seq in test_cases:
        if isinstance(seq[0], tuple):
            try:
                result = get_center_index(*seq[:1])
                print(f"Input {seq}: Result {result}")
            except Exception as e:
                print(f"Input {seq}: Error {e.__class__.__name__} - Expected")
        else:
            expected = seq[0] if isinstance(seq, list) and len(seq) > 1 else None
            try:
                result = get_center_index(*seq[:2])
                print(f"Input {seq}: Result {result}")
            except Exception as e:
                error_type = type(e).__name__
                expected_error = seq[0] if isinstance(seq, tuple) and len(seq) > 1 else None
                if not (expected is None or expected == error_type):
                    print(f"Input {seq}: Unexpected Error")