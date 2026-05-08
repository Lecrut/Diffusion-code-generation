def find_indices(data, target):
    indices = []
    for i, value in enumerate(data):
        if value == target:
            indices.append(i)
    return indices
if __name__ == '__main__':
    sample_list = [1, 5, 2, 5, 8, 5, 3]
    target_value = 5
    result = find_indices(sample_list, target_value)
    print(result)
    sample_list_2 = [10, 20, 10, 30, 10]
    target_value_2 = 10
    result_2 = find_indices(sample_list_2, target_value_2)
    print(result_2)
    sample_list_3 = [1, 2, 3, 4, 5]
    target_value_3 = 99
    result_3 = find_indices(sample_list_3, target_value_3)
    print(result_3)