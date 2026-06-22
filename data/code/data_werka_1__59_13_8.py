def get_central_item(sequence):
    if not sequence:
        return None
    length = len(sequence)
    mid_index = length // 2
    if length % 2 == 0:
        return (sequence[mid_index - 1], sequence[mid_index])
    else:
        return sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_1 = [7, 8, 9, 10, 11]
    sample_sequence_2 = [22, 33, 44, 55, 66, 77]
    sample_sequence_3 = []
    print(get_central_item(sample_sequence_1))
    print(get_central_item(sample_sequence_2))
    print(get_central_item(sample_sequence_3))