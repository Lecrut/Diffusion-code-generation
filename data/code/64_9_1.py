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