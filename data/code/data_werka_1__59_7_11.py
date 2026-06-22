def find_middle(sequence):
    if not sequence:
        raise ValueError('Sequence cannot be empty')
    n = len(sequence)
    middle_index = n // 2
    return sequence[middle_index]
if __name__ == '__main__':
    try:
        sample_sequence_odd = [1, 3, 5, 7, 9]
        print(find_middle(sample_sequence_odd))
        sample_sequence_even = [2, 4, 6, 8]
        print(find_middle(sample_sequence_even))
        empty_sequence = []
        print(find_middle(empty_sequence))
    except ValueError as e:
        print(e)