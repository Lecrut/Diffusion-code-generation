def get_central_item(sequence):
    if not sequence:
        return None
    length = len(sequence)
    mid_index = length // 2
    is_even_length = (length % 2 == 0)
    central_items = sequence[mid_index] if not is_even_length else (sequence[mid_index - 1], sequence[mid_index])
    return central_items

if __name__ == '__main__':
    sample_sequence_1 = [7, 8, 9]
    sample_sequence_2 = [14, 15, 16, 17]
    sample_sequence_3 = []
    print(get_central_item(sample_sequence_1))
    print(get_central_item(sample_sequence_2))
    print(get_central_item(sample_sequence_3))