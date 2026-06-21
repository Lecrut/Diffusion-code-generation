def get_center_item(sequence):
    if not sequence:
        raise ValueError("Sequence must not be empty")
    length = len(sequence)
    if length % 2 == 0:
        return [sequence[length // 2 - 1], sequence[length // 2]]
    else:
        return sequence[length // 2]

if __name__ == '__main__':
    print(get_center_item([1, 2, 3, 4, 5]))
    print(get_center_item([1, 2, 3, 4]))
    print(get_center_item(['a', 'b', 'c']))
    print(get_center_item([42]))
    print(get_center_item([1, 2]))