def get_element(sequence, index):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError('The sequence must be a list or tuple.')
    if not isinstance(index, int):
        raise TypeError('The index must be an integer.')
    if index < 0 or index >= len(sequence):
        raise IndexError('The index is out of range.')
    return sequence[index]
if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    sample_tuple = ('x', 'y', 'z', 'w', 'v')
    try:
        print(get_element(sample_list, 2))
    except Exception as e:
        print(e)
    try:
        print(get_element(sample_tuple, 4))
    except Exception as e:
        print(e)