def find_middle_index(sequence):
    if not sequence:
        return None
    length = len(sequence)
    if length % 2 == 0:
        middle_idx = (length // 2) - 1
    else:
        middle_idx = length // 2
    return middle_idx
if __name__ == '__main__':
    test_cases = [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        ['a', 'b'],
        ['x', 'y', 'z']
    ]
    for seq in test_cases:
        idx = find_middle_index(seq)
        if idx is not None:
            print(f"Sequence {seq} -> Middle Index: {idx}, Value: {seq[idx]}")
        else:
            print(f"Sequence {seq} -> No middle index (empty)")