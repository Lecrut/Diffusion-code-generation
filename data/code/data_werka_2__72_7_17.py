def compare_at_index(first_sequence, second_sequence, target_index):
    if target_index < 0:
        raise ValueError("Index must be non-negative")
    if target_index >= len(first_sequence):
        raise ValueError("Index out of range for first sequence")
    if target_index >= len(second_sequence):
        raise ValueError("Index out of range for second sequence")
    return first_sequence[target_index] <= second_sequence[target_index]

if __name__ == '__main__':
    seq_one = [1, 3, 5, 7]
    seq_two = [2, 2, 6, 8]
    pos = 1
    val = compare_at_index(seq_one, seq_two, pos)
    print(val)