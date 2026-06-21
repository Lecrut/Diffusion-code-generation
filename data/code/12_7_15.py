def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    length = len(sequence)
    middle_index = length // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_middle_element(sample_list))
    sample_tuple = (10, 20, 30, 40)
    print(get_middle_element(sample_tuple))
    sample_string = "abcdefg"
    print(get_middle_element(sample_string))
    sample_even = [1, 2, 3, 4]
    print(get_middle_element(sample_even))
    single_element = [42]
    print(get_middle_element(single_element))