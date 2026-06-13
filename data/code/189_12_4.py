def remove_all_occurrences(input_list, element_to_remove):
    new_list = [item for item in input_list if item != element_to_remove]
    for i in range(len(input_list)):
        if i < len(new_list):
            input_list[i] = new_list[i]
    return input_list
if __name__ == '__main__':
    my_list = [1, 2, 3, 2, 4, 2, 5]
    element = 2
    result_list = remove_all_occurrences(my_list, element)
    print(result_list)