def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    length = len(sequence)
    mid_index = length // 2
    if length % 2 == 1:
        return sequence[mid_index]
    else:
        return sequence[mid_index - 1], sequence[mid_index]

if __name__ == '__main__':
    odd_seq = [1, 2, 3, 4, 5]
    even_seq = [1, 2, 3, 4, 5, 6]
    single_seq = [42]
    two_seq = [10, 20]
    empty_seq = []

    print(get_middle_element(odd_seq))
    print(get_middle_element(even_seq))
    print(get_middle_element(single_seq))
    print(get_middle_element(two_seq))
    try:
        get_middle_element(empty_seq)
    except ValueError as e:
        print(e)