def get_middle_item(sequence):
    if not isinstance(sequence, (list, tuple, str)):
        raise TypeError("Input must be a sequence")
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence is empty")
    middle_index = length // 2
    if length % 2 == 0:
        return (sequence[middle_index - 1], sequence[middle_index])
    else:
        return sequence[middle_index]

if __name__ == '__main__':
    print(get_middle_item([1, 2, 3]))
    print(get_middle_item([1, 2, 3, 4]))
    print(get_middle_item("hello"))
    print(get_middle_item("worlds"))
    print(get_middle_item([42]))
    print(get_middle_item((1, 2, 3, 4, 5)))