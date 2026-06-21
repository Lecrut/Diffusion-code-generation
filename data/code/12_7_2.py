def get_middle_element(sequence):
    if len(sequence) == 0:
        raise ValueError("Sequence cannot be empty")
    mid_index = len(sequence) // 2
    if len(sequence) % 2 == 0:
        return sequence[mid_index]
    else:
        return sequence[mid_index]

if __name__ == '__main__':
    test_list_odd = [1, 2, 3, 4, 5]
    test_list_even = [10, 20, 30, 40]
    test_string_odd = "hello"
    test_string_even = "world!"
    test_tuple_odd = (100, 200, 300)
    test_tuple_even = (1, 2)
    print(get_middle_element(test_list_odd))
    print(get_middle_element(test_list_even))
    print(get_middle_element(test_string_odd))
    print(get_middle_element(test_string_even))
    print(get_middle_element(test_tuple_odd))
    print(get_middle_element(test_tuple_even))