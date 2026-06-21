def get_middle_item(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    length = len(sequence)
    index = length // 2
    return sequence[index]

if __name__ == '__main__':
    test_data_1 = [1, 2, 3, 4, 5]
    result_1 = get_middle_item(test_data_1)
    print(result_1)
    test_data_2 = [10, 20, 30, 40]
    result_2 = get_middle_item(test_data_2)
    print(result_2)
    test_data_3 = ["a", "b", "c"]
    result_3 = get_middle_item(test_data_3)
    print(result_3)