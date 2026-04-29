def add_item_efficiently(data: list, item: any) -> None:
    data.append(item)

if __name__ == '__main__':
    initial_list = [10, 20, 30]
    item_to_add = 40
    
    print(initial_list)
    
    add_item_efficiently(initial_list, item_to_add)
    
    print(initial_list)
    
    initial_list_two = ['a', 'b']
    item_two = 'c'
    
    print(initial_list_two)
    
    add_item_efficiently(initial_list_two, item_two)
    
    print(initial_list_two)