def store_unique_items(item_iterable):
    result_dict = {}
    for item in item_iterable:
        if item not in result_dict:
            result_dict[item] = item
    return result_dict
if __name__ == '__main__':
    sample_items = ["apple", "banana", "apple", "orange", "banana", "grape"]
    unique_items_dict = store_unique_items(sample_items)
    print(unique_items_dict)