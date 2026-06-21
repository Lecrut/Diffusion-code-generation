def check_item_existence(item, string_list):
    if not isinstance(item, int) or not all(isinstance(x, int) for x in string_list):
        raise ValueError("Item and list elements must be integers.")
    return item in string_list

if __name__ == '__main__':
    target_item = 3
    data_list = [1, 2, 3, 4, 5]
    result = check_item_existence(target_item, data_list)
    print(f"Does {target_item} exist in the list? {result}")
    
    target_item_2 = 6
    data_list_2 = [10, 20, 30, 40, 50]
    result_2 = check_item_existence(target_item_2, data_list_2)
    print(f"Does {target_item_2} exist in the list? {result_2}")