def get_central_item(sequence):
    if not sequence:
        raise ValueError('The sequence is empty')
    
    length = len(sequence)
    mid_index = length // 2
    
    if length % 2 == 0:
        central_items = {'first': sequence[mid_index - 1], 'second': sequence[mid_index]}
        return (central_items['first'] + central_items['second']) / 2
    else:
        return sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [3, 6, 9, 12, 15]
    sample_sequence_even = [4, 8, 12, 16, 20, 24]
    
    try:
        print(get_central_item(sample_sequence_odd))
        print(get_central_item(sample_sequence_even))
    except ValueError as e:
        print(e)