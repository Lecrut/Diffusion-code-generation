def find_first_occurrence(data_list, target):
    for i in range(len(data_list)):
        if data_list[i] == target:
            return i
    return -1
if __name__ == '__main__':
    my_list = [10, 25, 30, 45, 25, 50]
    target_value = 25
    index = find_first_occurrence(my_list, target_value)
    print(index)
    my_list_2 = [1, 5, 8, 3, 9]
    target_value_2 = 10
    index_2 = find_first_occurrence(my_list_2, target_value_2)
    print(index_2)
    my_list_3 = [1, 2, 3]
    target_value_3 = 4
    index_3 = find_first_occurrence(my_list_3, target_value_3)
    print(index_3)