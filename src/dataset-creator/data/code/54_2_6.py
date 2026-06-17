def find_middle_index(sequence):
    if not sequence:
        return None
    length = len(sequence)
    if length % 2 == 0:
        middle_idx = (length // 2) - 1
        return [middle_idx, middle_idx + 1]
    else:
        middle_idx = length // 2
        return [middle_idx]
if __name__ == '__main__':
    test_cases = [[], [1], [1, 2], [1, 2, 3]]
    for seq in test_cases:
        result = find_middle_index(seq)
        print(f"Input: {seq}, Output Indexes: {result}")