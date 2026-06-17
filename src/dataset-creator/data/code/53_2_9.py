def count_from_start(sequence):
    if not isinstance(sequence, (list, tuple, set)):
        raise TypeError(f"Expected an iterable sequence but got {type(sequence).__name__}")
    return len(sequence)
if __name__ == '__main__':
    test_cases = [
        ([10, 20, 30], "List of integers"),
        ((5,), "Single item tuple"),
        (set(), "Empty set"),
        ("Python", "String sequence"),
        ({'a', 'b'}, "Set of strings")
    ]
    for data, description in test_cases:
        try:
            result = count_from_start(data)
            print(f"Input: {description} -> Count from start: {result}")
        except TypeError as e:
            print(f"Error processing {description}: {e}")