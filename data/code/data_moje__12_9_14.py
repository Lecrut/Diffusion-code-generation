def get_middle_item(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    length = len(sequence)
    middle_index = length // 2
    if length % 2 == 0:
        return sequence[middle_index]
    return sequence[middle_index]

if __name__ == '__main__':
    test_data_1 = [1, 2, 3, 4, 5]
    test_data_2 = [10, 20, 30, 40]
    test_data_3 = ['a', 'b', 'c']
    test_data_4 = [42, 99]
    test_data_5 = ['single']
    result_1 = get_middle_item(test_data_1)
    result_2 = get_middle_item(test_data_2)
    result_3 = get_middle_item(test_data_3)
    result_4 = get_middle_item(test_data_4)
    result_5 = get_middle_item(test_data_5)
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
    print(result_5)