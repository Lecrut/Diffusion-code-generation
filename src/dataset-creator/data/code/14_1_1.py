def store_item_names(item_names):
    item_dict = {}
    for item in item_names:
        item_dict[item] = None
    return item_dict
if __name__ == '__main__':
    sample_names = ["apple", "banana", "cherry", "date"]
    result = store_item_names(sample_names)
    print(result)