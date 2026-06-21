def get_middle_element(sequence):
    if not isinstance(sequence, (list, tuple, str, range, bytes, bytearray)):
        raise TypeError("Input must be a sequence type such as list, tuple, string, or bytes.")
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence cannot be empty.")
    if length % 2 == 1:
        return sequence[length // 2]
    mid_index = length // 2
    return sequence[mid_index - 1], sequence[mid_index]

if __name__ == "__main__":
    test_list_odd = [1, 2, 3, 4, 5]
    test_tuple_even = (10, 20, 30, 40)
    test_string_odd = "hello"
    test_string_even = "python"
    empty_list = []
    invalid_input = 123
    print(get_middle_element(test_list_odd))
    print(get_middle_element(test_tuple_even))
    print(get_middle_element(test_string_odd))
    print(get_middle_element(test_string_even))
    try:
        get_middle_element(empty_list)
    except ValueError as e:
        print(str(e))
    try:
        get_middle_element(invalid_input)
    except TypeError as e:
        print(str(e))