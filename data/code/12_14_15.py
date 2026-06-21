def get_middle_element(sequence):
    if not hasattr(sequence, '__getitem__') or not hasattr(sequence, '__len__'):
        raise TypeError("Input must be a sequence with indexable access and length")
    length = len(sequence)
    if length == 0:
        raise ValueError("Cannot get middle element of an empty sequence")
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        left_index = length // 2 - 1
        right_index = length // 2
        return (sequence[left_index], sequence[right_index])

if __name__ == '__main__':
    odd_sequence = [1, 2, 3, 4, 5]
    print(get_middle_element(odd_sequence))
    even_sequence = [1, 2, 3, 4]
    print(get_middle_element(even_sequence))
    single_element = [42]
    print(get_middle_element(single_element))
    two_elements = [10, 20]
    print(get_middle_element(two_elements))
    string_sequence = "abcdef"
    print(get_middle_element(string_sequence))
    string_odd = "abcde"
    print(get_middle_element(string_odd))
    empty_list = []
    try:
        get_middle_element(empty_list)
    except ValueError as e:
        print(repr(e))
    invalid_input = 123
    try:
        get_middle_element(invalid_input)
    except TypeError as e:
        print(repr(e))