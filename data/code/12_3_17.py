def find_middle_element(data):
    length = len(data)
    if length == 0:
        return None
    middle_index = length // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = [1, 2, 3, 4]
    sample_list_3 = []
    result_1 = find_middle_element(sample_list_1)
    result_2 = find_middle_element(sample_list_2)
    result_3 = find_middle_element(sample_list_3)
    print(result_1)
    print(result_2)
    print(result_3)