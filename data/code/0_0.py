def add_item_to_list(data: list, item: object) -> list:
    data.append(item)
    return data

if __name__ == '__main__':
    initial_list = [1, 2, 3]
    new_item = 4
    result_list = add_item_to_list(initial_list, new_item)
    print(result_list)

    initial_list_2 = ['a', 'b']
    new_item_2 = 'c'
    result_list_2 = add_item_to_list(initial_list_2, new_item_2)
    print(result_list_2)