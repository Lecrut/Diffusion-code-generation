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
    result = insert_element(initial_list, new_element, target_index)
    print(result)

    initial_list_2 = ['a', 'b', 'c']
    new_element_2 = 'x'
    target_index_2 = 0
    result_2 = insert_element(initial_list_2, new_element_2, target_index_2)
    print(result_2)

    initial_list_3 = [10, 20]
    new_element_3 = 30
    target_index_3 = 5
    result_3 = insert_element(initial_list_3, new_element_3, target_index_3)
    print(result_3)