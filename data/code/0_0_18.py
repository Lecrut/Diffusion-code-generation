def add_item_to_list(data_list: list, item) -> list:
    data_list.append(item)
    return data_list

if __name__ == '__main__':
    initial_list = [1, 2, 3]
    item_to_add = 4
    result = add_item_to_list(initial_list, item_to_add)
    print(result)