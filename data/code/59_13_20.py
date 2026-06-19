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
    sample_sequence_1 = [7, 8, 9]
    sample_sequence_2 = [14, 28, 42, 56]
    sample_sequence_3 = []
    print(get_central_item(sample_sequence_1))
    print(get_central_item(sample_sequence_2))
    print(get_central_item(sample_sequence_3))