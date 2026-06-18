def get_center_index(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be an iterable sequence like list or tuple.")
    length = len(sequence)
    return length // 2
if __name__ == '__main__':
    test_cases = [
        ([10], "Single element"),
        ([10, 20], "Even elements start"),
        ([10, 20, 30], "Odd elements middle"),
        ((5,), "Tuple single"),
        ((), "Empty tuple")
    ]
    for seq, desc in test_cases:
        try:
            idx = get_center_index(seq)
            print(f"{desc}: Index {idx}")
        except Exception as e:
            print(f"{desc}: Error - {e}")