def get_central_item(sequence):
    if not sequence:
        return None
    length = len(sequence)
    mid_index = length // 2
    is_even_length = (length % 2 == 0)
    if is_even_length:
        return (sequence[mid_index - 1], sequence[mid_index])
    else:
        return sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_1 = [7, 14, 21, 28, 35]
    sample_sequence_2 = [10, 20, 30, 40, 50, 60]
    sample_sequence_3 = []
    print(get_central_item(sample_sequence_1))
    print(get_central_item(sample_sequence_2))
    print(get_central_item(sample_sequence_3))