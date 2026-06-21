def get_center_element(sequence):
    if not sequence:
        return None
    mid_index = len(sequence) // 2
    if len(sequence) % 2 == 1:
        return sequence[mid_index]
    else:
        return sequence[mid_index - 1]

if __name__ == '__main__':
    test_list = [10, 20, 30, 40, 50]
    test_tuple = (1, 2, 3, 4, 5, 6)
    result_list = get_center_element(test_list)
    result_tuple = get_center_element(test_tuple)
    print(result_list)
    print(result_tuple)