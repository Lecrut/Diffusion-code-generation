def find_middle_item(data):
    MIDDLE_INDEX_CONSTANT = 1
    n = len(data)
    middle_index = (n - MIDDLE_INDEX_CONSTANT) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [10, 20, 30, 40]
    sample_list_3 = [100]
    sample_list_4 = [5, 15, 25, 35, 45, 55]
    print(find_middle_item(sample_list_1))
    print(find_middle_item(sample_list_2))
    print(find_middle_item(sample_list_3))
    print(find_middle_item(sample_list_4))