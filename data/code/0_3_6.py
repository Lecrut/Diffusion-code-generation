def insert_element(data: list, element: any, index: int) -> list:
    try:
        data.insert(index, element)
        return data
    except IndexError:
        return data

def insert_safe(data: list, element: any, index: int) -> list:
    if index < 0 or index > len(data):
        return data
    data.insert(index, element)
    return data

if __name__ == '__main__':
    initial_list = [10, 20, 30, 40]
    new_value = 25
    valid_index = 2
    invalid_index_high = 10
    invalid_index_low = -1

    result_safe = insert_safe(initial_list.copy(), new_value, valid_index)
    print(result_safe)

    result_safe_high = insert_safe(initial_list.copy(), new_value, invalid_index_high)
    print(result_safe_high)

    result_safe_low = insert_safe(initial_list.copy(), new_value, invalid_index_low)
    print(result_safe_low)