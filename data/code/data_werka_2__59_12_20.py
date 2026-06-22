def get_central_item(sequence):
    if not sequence:
        raise ValueError('The sequence is empty')
    length = len(sequence)
    mid_index = length // 2
    if length % 2 == 0:
        return (sequence[mid_index - 1] + sequence[mid_index]) / 2
    else:
        return sequence[mid_index]
if __name__ == '__main__':
    sample_sequence_odd = [1, 3, 5, 7, 9]
    sample_sequence_even = [2, 4, 6, 8, 10, 12]
    print(get_central_item(sample_sequence_odd))
    print(get_central_item(sample_sequence_even))