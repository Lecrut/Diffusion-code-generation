def add_item_to_list(data: list, item: object) -> list:
    data.append(item)
    return data

if __name__ == '__main__':
    initial_list = [1, 2, 3]
    item_to_add = 4
    result = add_item_to_list(initial_list, item_to_add)
    print(result)

    initial_list_2 = ['a', 'b']
    item_to_add_2 = 'c'
    result_2 = add_item_to_list(initial_list_2, item_to_add_2)
    print(result_2)