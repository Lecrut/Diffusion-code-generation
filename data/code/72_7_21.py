def compare_at_index(first_sequence, second_sequence, target_index):
    if target_index < 0:
        raise ValueError("Index cannot be negative")
    if target_index >= len(first_sequence):
        raise ValueError("Index out of range for first list")
    if target_index >= len(second_sequence):
        raise ValueError("Index out of range for second list")
    return first_sequence[target_index] <= second_sequence[target_index]

if __name__ == '__main__':
    values_one = [1, 2, 3]
    values_two = [2, 1, 4]
    pos = 1
    result = compare_at_index(values_one, values_two, pos)
    print(result)