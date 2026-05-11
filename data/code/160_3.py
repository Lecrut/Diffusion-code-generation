def store_unique_items(item_list):
    item_dict = {}
    for item in item_list:
        if item not in item_dict:
            item_dict[item] = True
    return item_dict
if __name__ == '__main__':
    sample_items = ["apple", "banana", "apple", "orange", "banana", "grape"]
    result_dict = store_unique_items(sample_items)
    print(result_dict)