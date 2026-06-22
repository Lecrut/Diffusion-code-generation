def validate_sequence(sequence):
    if not sequence:
        raise ValueError('The sequence is empty')
    if not isinstance(sequence, (list, tuple)):
        raise TypeError('The input must be a list or a tuple')

def get_central_item(sequence):
    validate_sequence(sequence)
    length = len(sequence)
    mid_index = length // 2
    if length % 2 == 0:
        return (sequence[mid_index - 1] + sequence[mid_index]) / 2
    else:
        return sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [15, 30, 45, 60, 75]
    sample_sequence_even = [10, 20, 30, 40, 50, 60]
    print(get_central_item(sample_sequence_odd))
    print(get_central_item(sample_sequence_even))