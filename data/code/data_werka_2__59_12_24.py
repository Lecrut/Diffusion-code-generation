def validate_sequence(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError('The input must be a list or a tuple')
    if not sequence:
        raise ValueError('The sequence is empty')

def get_central_item(sequence):
    validate_sequence(sequence)
    length = len(sequence)
    mid_index = length // 2
    if length % 2 == 0:
        return (sequence[mid_index - 1] + sequence[mid_index]) / 2
    else:
        return sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [9, 18, 27, 36, 45]
    sample_sequence_even = [3, 6, 9, 12, 15, 18]
    print(get_central_item(sample_sequence_odd))
    print(get_central_item(sample_sequence_even))