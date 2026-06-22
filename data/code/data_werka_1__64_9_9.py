def find_final_index(data, target):
    for i in range(len(data) - 1, -1, -1):
        if data[i] == target:
            return i
    return -1

if __name__ == '__main__':
    my_list = [1, 5, 2, 8, 5, 3, 5, 9]
    target_value = 5
    final_index = find_final_index(my_list, target_value)
    print(final_index)

    another_list = ['a', 'b', 'c', 'd', 'c']
    target_value_2 = 'c'
    final_index_2 = find_final_index(another_list, target_value_2)
    print(final_index_2)

    no_match_list = [7, 8, 9]
    target_value_3 = 10
    final_index_3 = find_final_index(no_match_list, target_value_3)
    print(final_index_3)