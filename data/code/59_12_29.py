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
    sample_sequence_odd = [11, 22, 33, 44, 55]
    sample_sequence_even = [6, 12, 18, 24, 30, 36]
    print(get_central_item(sample_sequence_odd))
    print(get_central_item(sample_sequence_even))