def get_list_element(data_list, index):
    try:
        return data_list[index]
    except IndexError:
        return "Index out of bounds"
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    target_index_valid = 2
    target_index_invalid = 5
    result_valid = get_list_element(my_list, target_index_valid)
    result_invalid = get_list_element(my_list, target_index_invalid)
    print(f"List: {my_list}")
    print(f"Attempting to access index {target_index_valid}: {result_valid}")
    print(f"Attempting to access index {target_index_invalid}: {result_invalid}")