def concatenate_lists(input_list1, input_list2):
    return input_list1 + input_list2

if __name__ == '__main__':
    list_x = [10, 20, 30]
    list_y = [40, 50, 60]
    output = concatenate_lists(list_x, list_y)
    print(output)