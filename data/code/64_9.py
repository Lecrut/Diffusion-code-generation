def find_final_index(data, target):
    last_index = -1
    for i in range(len(data)):
        if data[i] == target:
            last_index = i
    return last_index
if __name__ == '__main__':
    my_list = [1, 5, 2, 8, 5, 3, 5, 9]
    target_value = 5
    final_index = find_final_index(my_list, target_value)
    print(final_index)
    my_list_2 = [10, 20, 30, 20, 40, 20]
    target_value_2 = 20
    final_index_2 = find_final_index(my_list_2, target_value_2)
    print(final_index_2)
    my_list_3 = [1, 2, 3, 4]
    target_value_3 = 99
    final_index_3 = find_final_index(my_list_3, target_value_3)
    print(final_index_3)