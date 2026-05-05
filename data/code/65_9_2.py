def find_and_retrieve(data_list, position):
    if 0 <= position < len(data_list):
        return data_list[position]
    else:
        return None
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    target_position = 2
    result = find_and_retrieve(my_list, target_position)
    print(result)
    target_position_out_of_bounds = 10
    result_out_of_bounds = find_and_retrieve(my_list, target_position_out_of_bounds)
    print(result_out_of_bounds)
    target_position_first = 0
    result_first = find_and_retrieve(my_list, target_position_first)
    print(result_first)