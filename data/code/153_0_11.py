def check_item_existence(item, string_list):
    if not isinstance(item, int) or not all(isinstance(x, int) for x in string_list):
        raise ValueError("Both item and all elements in string_list must be integers.")
    
    return item in string_list

if __name__ == '__main__':
    target_item = 3
    data_list = [1, 2, 3, 4, 5]
    result = check_item_existence(target_item, data_list)
    print(f"Does {target_item} exist in the list? {result}")