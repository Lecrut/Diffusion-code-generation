def add_item_efficiently(data_list: list, item) -> None:
    data_list.append(item)

if __name__ == '__main__':
    initial_list = [10, 20, 30]
    item_to_add = 40
    
    print(initial_list)
    
    add_item_efficiently(initial_list, item_to_add)
    
    print(initial_list)