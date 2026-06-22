def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    if len(sequence) % 2 == 1:
        return sequence[len(sequence) // 2]
    return sequence[len(sequence) // 2 - 1]

if __name__ == '__main__':
    test_list = [10, 20, 30, 40, 50]
    print(get_middle_element(test_list))
    test_tuple = (1, 2, 3, 4, 5, 6, 7)
    print(get_middle_element(test_tuple))
    test_string = "hello"
    print(get_middle_element(test_string))
    test_even_list = [1, 2, 3, 4]
    print(get_middle_element(test_even_list))
    test_range = range(100)
    print(get_middle_element(test_range))