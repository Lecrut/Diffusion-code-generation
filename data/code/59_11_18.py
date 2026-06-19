def find_middle_element(sequence):
    length = len(sequence)
    if length == 0:
        return None
    middle_index = length // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_list_odd = [7, 2, 5, 3, 9]
    sample_list_even = [1, 4, 6, 8, 10, 12]
    single_element_list = [42]
    empty_list = []

    print(f"Middle element of odd list: {find_middle_element(sample_list_odd)}")
    print(f"Middle element of even list: {find_middle_element(sample_list_even)}")
    print(f"Middle element of single-element list: {find_middle_element(single_element_list)}")
    print(f"Middle element of empty list: {find_middle_element(empty_list)}")