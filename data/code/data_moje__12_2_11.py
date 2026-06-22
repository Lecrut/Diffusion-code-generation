def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    mid_index = len(sequence) // 2
    return sequence[mid_index]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = [1, 2, 3, 4]
    sample_tuple = ('a', 'b', 'c', 'd', 'e')
    sample_string = "hello"

    print(get_middle_element(sample_list_1))
    print(get_middle_element(sample_list_2))
    print(get_middle_element(sample_tuple))
    print(get_middle_element(sample_string))