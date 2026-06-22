def get_middle_item(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    length = len(sequence)
    middle_index = length // 2
    if length % 2 == 1:
        return sequence[middle_index]
    else:
        return sequence[middle_index - 1]

if __name__ == "__main__":
    test_list_odd = [1, 2, 3, 4, 5]
    test_list_even = [10, 20, 30, 40]
    test_tuple = ("a", "b", "c", "d", "e", "f")
    
    result_odd = get_middle_item(test_list_odd)
    result_even = get_middle_item(test_list_even)
    result_tuple = get_middle_item(test_tuple)
    
    print(result_odd)
    print(result_even)
    print(result_tuple)