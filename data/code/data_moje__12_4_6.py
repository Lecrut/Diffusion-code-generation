def get_middle_value(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    sorted_sequence = sorted(sequence)
    length = len(sorted_sequence)
    mid_index = length // 2
    if length % 2 == 1:
        return sorted_sequence[mid_index]
    else:
        left = sorted_sequence[mid_index - 1]
        right = sorted_sequence[mid_index]
        if isinstance(left, int) and isinstance(right, int):
            return (left + right) // 2
        elif isinstance(left, float) or isinstance(right, float):
            return (left + right) / 2
        else:
            return (left + right) / 2

if __name__ == '__main__':
    odd_length_list = [3, 1, 4, 1, 5]
    even_length_list = [2, 3, 4, 5]
    single_element_list = [42]
    two_element_list = [10, 20]

    print(get_middle_value(odd_length_list))
    print(get_middle_value(even_length_list))
    print(get_middle_value(single_element_list))
    print(get_middle_value(two_element_list))