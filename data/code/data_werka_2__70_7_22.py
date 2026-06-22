def get_boundary_items(sequence):
    if not hasattr(sequence, '__getitem__') or not hasattr(sequence, '__len__'):
        raise ValueError("Input must be a sequence type")
    length = len(sequence)
    if length == 0:
        return (None, None)
    if length == 1:
        return (sequence[0], sequence[0])
    return (sequence[0], sequence[-1])

if __name__ == '__main__':
    data_types = {
        'list': [1, 2, 3],
        'tuple': (4, 5, 6),
        'string': "abc",
        'empty_list': [],
        'single_item': [42]
    }
    for name, seq in data_types.items():
        print(get_boundary_items(seq))