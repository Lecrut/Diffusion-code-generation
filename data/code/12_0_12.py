def get_middle_element(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence must not be empty")
    mid_index = length // 2
    if length % 2 == 1:
        return sequence[mid_index]
    else:
        return sequence[mid_index - 1], sequence[mid_index]

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3, 4, 5]))
    print(get_middle_element([1, 2, 3, 4]))
    print(get_middle_element([42]))
    print(get_middle_element([1, 2]))