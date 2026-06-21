def get_central_item(sequence):
    if not sequence:
        raise ValueError('The sequence is empty')
    
    length = len(sequence)
    mid_index = length // 2
    
    if length % 2 == 0:
        first_mid = sequence[mid_index - 1]
        second_mid = sequence[mid_index]
        central_value = (first_mid + second_mid) / 2
    else:
        central_value = sequence[mid_index]
    
    return central_value

if __name__ == '__main__':
    sample_sequence_odd = [3, 6, 9, 12, 15]
    sample_sequence_even = [4, 8, 12, 16, 20, 24]
    
    try:
        print(get_central_item(sample_sequence_odd))
        print(get_central_item(sample_sequence_even))
    except ValueError as e:
        print(e)