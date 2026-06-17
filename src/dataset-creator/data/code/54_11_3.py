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
        ((), -1)
    ]
    for seq, expected in test_cases:
        result = get_center_index(seq)
        print(f"Input: {seq}, Expected Center Index: {expected}, Got: {result}")