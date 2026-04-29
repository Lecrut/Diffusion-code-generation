def insert_element(data_list: list, new_element: object, index: int) -> list:
    MAX_INDEX = 1000000
    if not (0 <= index <= len(data_list)):
        return data_list
    try:
        data_list.insert(index, new_element)
        return data_list
    except IndexError:
        return data_list

if __name__ == '__main__':
    initial_list = [10, 20, 30, 40]
    new_val = 25
    valid_index = 2