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
    sample_sequence_1 = [1, 3, 5, 7, 9]
    sample_sequence_2 = [2, 4, 6, 8]
    sample_sequence_3 = []
    try:
        print(get_central_item(sample_sequence_1))
        print(get_central_item(sample_sequence_2))
        print(get_central_item(sample_sequence_3))
    except ValueError as e:
        print(e)