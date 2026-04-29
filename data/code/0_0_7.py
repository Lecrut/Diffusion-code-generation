def add_item_to_list(data_list: list, item: object) -> None:
    data_list.append(item)

if __name__ == '__main__':
    initial_list = [1, 2, 3]
    item_to_add = 4
    
    print(f"initial_list={initial_list}")
    
    add_item_to_list(initial_list, item_to_add)
    
    final_list = initial_list
    print(f"final_list={final_list}")