def insert_element(data_list: list, new_element: any, index: int) -> list:
    MAX_INDEX = float('inf')
    try:
        data_list.insert(index, new_element)
        return data_list
    except IndexError:
        return data_list

if __name__ == '__main__':
    initial_list = [10, 20, 30, 40]
    new_value = 25
    insert_index = 2

    result = insert_element(initial_list, new_value, insert_index)

    print(result)