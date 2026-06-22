def find_final_index(data, target):
    if not isinstance(data, list):
        raise TypeError("The data must be a list.")
    if not isinstance(target, (int, float, str)):
        raise ValueError("The target must be an integer, float, or string.")
    
    last_index = -1
    for index, element in enumerate(data):
        if element == target:
            last_index = index
    return last_index

if __name__ == '__main__':
    sample_list_1 = [1, 5, 2, 8, 5, 3, 5, 9]
    target_value_1 = 5
    print(find_final_index(sample_list_1, target_value_1))

    sample_list_2 = [10, 20, 30, 20, 40, 20]
    target_value_2 = 20
    print(find_final_index(sample_list_2, target_value_2))

    sample_list_3 = [1, 2, 3, 4]
    target_value_3 = 99
    print(find_final_index(sample_list_3, target_value_3))