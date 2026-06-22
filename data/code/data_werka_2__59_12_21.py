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
    sample_sequence_odd = [10, 20, 30, 40, 50]
    sample_sequence_even = [5, 15, 25, 35, 45, 55]
    print(get_central_item(sample_sequence_odd))
    print(get_central_item(sample_sequence_even))