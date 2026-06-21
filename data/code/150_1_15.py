def remove_item_from_list(input_list, target_item):
    if not input_list or target_item is None:
        return input_list
    
    return list(filter(lambda item: item != target_item, input_list))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    item_to_remove = 3
    result = remove_item_from_list(sample_list, item_to_remove)
    print(result)