def is_valid_index(sequence, index):
    return 0 <= index < len(sequence)

def get_element(sequence, index):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError('The sequence must be a list or a tuple.')
    if not is_valid_index(sequence, index):
        raise IndexError('Index out of range.')
    return sequence[index]
if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    sample_tuple = ('x', 'y', 'z', 'w', 'v')
    print(get_element(sample_list, 2))
    print(get_element(sample_tuple, 3))