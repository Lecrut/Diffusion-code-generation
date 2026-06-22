def get_middle_value(sequence):
    if len(sequence) == 0:
        raise ValueError("Sequence cannot be empty")
    sorted_sequence = sorted(sequence)
    mid_index = len(sorted_sequence) // 2
    if len(sorted_sequence) % 2 == 0:
        return (sorted_sequence[mid_index - 1] + sorted_sequence[mid_index]) / 2
    return sorted_sequence[mid_index]

if __name__ == '__main__':
    example_odd = [3, 1, 4, 1, 5]
    example_even = [10, 2, 8, 4]
    print(get_middle_value(example_odd))
    print(get_middle_value(example_even))