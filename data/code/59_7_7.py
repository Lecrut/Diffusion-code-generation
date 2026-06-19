def find_middle(sequence):
    n = len(sequence)
    if n == 0:
        raise ValueError('Sequence cannot be empty')
    middle_index = (n - 1) // 2
    return sequence[middle_index]
if __name__ == '__main__':
    sample_sequence_odd = [1, 2, 3, 4, 5]
    sample_sequence_even = [10, 20, 30, 40, 50, 60]
    print(find_middle(sample_sequence_odd))
    print(find_middle(sample_sequence_even))