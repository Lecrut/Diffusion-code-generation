def find_middle_index(sequence):
    if not sequence:
        return None
    length = len(sequence)
    if length % 2 == 0:
        mid_idx = (length // 2) - 1
        left_val, right_val = sequence[mid_idx], sequence[mid_idx + 1]
        if left_val <= right_val:
            return mid_idx
        else:
            return mid_idx + 1
    else:
        mid_idx = length // 2
        return mid_idx
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
        result = find_middle_index(seq)
        print(f"Input {seq} -> Middle Index Mark: {result}")