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
    sample_sequence_1 = [1, 2, 3, 4, 5]
    sample_sequence_2 = [10, 20, 30, 40]
    sample_sequence_3 = []
    print(get_central_item(sample_sequence_1))
    print(get_central_item(sample_sequence_2))
    print(get_central_item(sample_sequence_3))