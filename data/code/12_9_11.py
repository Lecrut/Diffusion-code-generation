def middle_item(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    length = len(sequence)
    if length % 2 == 0:
        raise ValueError("Sequence has even length, no single middle item")
    middle_index = length // 2
    return sequence[middle_index]

if __name__ == '__main__':
    print(middle_item([1, 2, 3]))
    print(middle_item([1, 2, 3, 4, 5]))
    print(middle_item(['a', 'b', 'c']))
    print(middle_item([42]))
    try:
        middle_item([])
    except ValueError as e:
        print(e)
    try:
        middle_item([1, 2])
    except ValueError as e:
        print(e)