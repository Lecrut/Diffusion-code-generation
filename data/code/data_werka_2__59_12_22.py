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
    sample_sequence_odd = [7, 14, 21, 28, 35]
    sample_sequence_even = [1, 2, 3, 4, 5, 6]
    
    try:
        print(get_central_item(sample_sequence_odd))
        print(get_central_item(sample_sequence_even))
    except ValueError as e:
        print(e)