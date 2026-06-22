def get_central_item(sequence):
    if not sequence:
        return None
    length = len(sequence)
    mid_index = length // 2
    is_even_length = (length % 2 == 0)
    
    if is_even_length:
        central_items = (sequence[mid_index - 1], sequence[mid_index])
    else:
        central_items = sequence[mid_index]
    
    return central_items

if __name__ == '__main__':
    sample_sequence_1 = [5, 15, 25, 35, 45]
    sample_sequence_2 = [100, 200, 300, 400, 500, 600]
    sample_sequence_3 = []
    
    print(get_central_item(sample_sequence_1))
    print(get_central_item(sample_sequence_2))
    print(get_central_item(sample_sequence_3))