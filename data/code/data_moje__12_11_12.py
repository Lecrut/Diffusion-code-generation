def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    length = len(sequence)
    mid_index = length // 2
    if length % 2 == 0:
        return (sequence[mid_index - 1], sequence[mid_index])
    return sequence[mid_index]

if __name__ == '__main__':
    test_tuple = (1, 2, 3, 4, 5)
    print(get_middle_element(test_tuple))
    test_empty = ()
    try:
        get_middle_element(test_empty)
    except ValueError as e:
        print(e)