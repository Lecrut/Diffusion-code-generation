def contains_item(data_list: list, target_item) -> bool:
    return target_item in data_list

if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    item_to_check = 8
    result = contains_item(sample_list, item_to_check)
    print(f"List: {sample_list}, Item: {item_to_check}, Result: {result}")