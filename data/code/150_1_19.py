def remove_item_from_list(input_list, target_item):
    return list(filter(lambda x: x != target_item, input_list))

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    item_to_remove = 30
    result = remove_item_from_list(sample_list, item_to_remove)
    print(f"Original list: {sample_list}")
    print(f"Item to remove: {item_to_remove}")
    print(f"New list: {result}")