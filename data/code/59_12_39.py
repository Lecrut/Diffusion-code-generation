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
    sample_sequence_even = [1, 3, 5, 7, 9, 11]
    sample_sequence_empty = []
    print('Central item of odd sequence:', get_central_item(sample_sequence_odd))
    print('Central item of even sequence:', get_central_item(sample_sequence_even))
    try:
        print('Central item of empty sequence:', get_central_item(sample_sequence_empty))
    except ValueError as e:
        print(e)