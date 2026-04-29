def insert_element(data: list, element: any, index: int) -> list:
    try:
        data.insert(index, element)
        return data
    except IndexError:
        return data

if __name__ == '__main__':
    initial_list = [1, 2, 3, 4]
    new_element = 99
    target_index = 2

    result_list = insert_element(initial_list, new_element, target_index)

    print(result_list)