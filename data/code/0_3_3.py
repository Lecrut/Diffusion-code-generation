def insert_at_index(data_list: list, new_element: any, index: int) -> list:
    try:
        data_list.insert(index, new_element)
        return data_list
    except IndexError:
        return data_list

if __name__ == '__main__':
    initial_list = [10, 20, 30]
    new_value = 25
    valid_index = 1
    invalid_index = 100

    result_valid = insert_at_index(initial_list.copy(), new_value, valid_index)
    result_invalid = insert_at_index(initial_list.copy(), new_value, invalid_index)

    print(f"result_valid: {result_valid}")