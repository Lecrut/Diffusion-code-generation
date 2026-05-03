def get_list_element(data_list, index):
    try:
        return data_list[index]
    except IndexError:
        return "Index out of bounds"
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index = 5
    result_valid = get_list_element(my_list, valid_index)
    result_invalid = get_list_element(my_list, invalid_index)
    print(f"List: {my_list}")
    print(f"Element at index {valid_index}: {result_valid}")
    print(f"Element at index {invalid_index}: {result_invalid}")