def get_central_item(sequence):
    EMPTY_SEQUENCE_ERROR = 'The sequence is empty'
    
    if not sequence:
        raise ValueError(EMPTY_SEQUENCE_ERROR)
    
    length = len(sequence)
    mid_index = length // 2
    
    if length % 2 == 0:
        return (sequence[mid_index - 1] + sequence[mid_index]) / 2
    else:
        return sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [15, 25, 35, 45, 55]
    sample_sequence_even = [10, 20, 30, 40, 50, 60]
    
    try:
        print(get_central_item(sample_sequence_odd))
        print(get_central_item(sample_sequence_even))
    except ValueError as e:
        print(e)