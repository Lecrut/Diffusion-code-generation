def store_item_names(item_names):
    item_dict = {}
    for name in item_names:
        item_dict[name] = name
    return item_dict
if __name__ == '__main__':
    sample_names = ["apple", "banana", "cherry", "date"]
    result = store_item_names(sample_names)
    print(result)