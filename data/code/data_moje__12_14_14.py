def get_middle_element(sequence):
    if not isinstance(sequence, (list, tuple, str)):
        raise TypeError("Input must be a list, tuple, or string")
    if len(sequence) == 0:
        raise ValueError("Input sequence cannot be empty")
    length = len(sequence)
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        mid_index = length // 2
        return sequence[mid_index]

if __name__ == '__main__':
    test_list_odd = [10, 20, 30, 40, 50]
    test_list_even = [10, 20, 30, 40]
    test_string_odd = "hello"
    test_string_even = "worlds"
    
    result1 = get_middle_element(test_list_odd)
    result2 = get_middle_element(test_list_even)
    result3 = get_middle_element(test_string_odd)
    result4 = get_middle_element(test_string_even)
    
    print(result1)
    print(result2)
    print(result3)
    print(result4)