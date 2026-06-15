def remove_elements(data_list, target):
    i = 0
    while i < len(data_list):
        if data_list[i] == target:
            data_list.pop(i)
        else:
            i += 1
    return data_list
if __name__ == '__main__':
    my_list = [1, 5, 2, 5, 8, 5, 3, 9]
    target_value = 5
    result_list = remove_elements(my_list, target_value)
    print(result_list)
    my_list_2 = [10, 20, 30, 40, 20, 50]
    target_value_2 = 20
    result_list_2 = remove_elements(my_list_2, target_value_2)
    print(result_list_2)
    my_list_3 = [1, 2, 3, 4, 5]
    target_value_3 = 99
    result_list_3 = remove_elements(my_list_3, target_value_3)
    print(result_list_3)