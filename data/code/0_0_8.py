def add_item_to_list(data: list, item: object) -> list:
    data.append(item)
    return data

if __name__ == '__main__':
    initial_list = [1, 2, 3]
    item_to_add = 4
    
    result = add_item_to_list(initial_list, item_to_add)
    
    print(result)