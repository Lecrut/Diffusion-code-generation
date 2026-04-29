def insert_element(data_list: list, new_element: object, index: int) -> list:
    try:
        data_list.insert(index, new_element)
        return data_list
    except IndexError:
        return data_list

if __name__ == '__main__':
    initial_list = [10, 20, 30, 40]