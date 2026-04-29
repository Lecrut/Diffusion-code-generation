def insert_element(data: list, element: any, index: int) -> list:
    try:
        data.insert(index, element)
        return data
    except IndexError:
        return data

def safe_insert(data: list, element: any, index: int) -> list:
    if index < 0 or index > len(data):
        return data
    try:
        data.insert(index, element)
        return data
    except IndexError:
        return data

def insert_element_safe(data: list, element: any, index: int) -> list:
    if index < 0 or index > len(data):
        return data
    data.insert(index, element)
    return data

if __name__ == '__main__':
    initial_list = [1, 2, 3, 4]
    new_element = 99
    valid_index = 2
    invalid_index = 10
    empty_list = []

    result1 = insert_element_safe(initial_list, new_element, valid_index)
    print(result1)

    result2 = insert_element_safe(initial_list, new_element, invalid_index)
    print(result2)

    result3 = insert_element_safe(empty_list, new_element, 0)
    print(result3)

    result4 = insert_element_safe(initial_list, 5, -1)
    print(result4)