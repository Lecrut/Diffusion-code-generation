def get_middle_element(sequence):
    length = len(sequence)
    if length == 0:
        return None
    middle_index = length // 2
    if length % 2 == 0:
        return (sequence[middle_index - 1], sequence[middle_index])
    else:
        return sequence[middle_index]

if __name__ == '__main__':
    odd_length_sequence = [1, 2, 3, 4, 5]
    even_length_sequence = [1, 2, 3, 4]
    empty_sequence = []
    single_element_sequence = [42]

    print(get_middle_element(odd_length_sequence))
    print(get_middle_element(even_length_sequence))
    print(get_middle_element(empty_sequence))
    print(get_middle_element(single_element_sequence))