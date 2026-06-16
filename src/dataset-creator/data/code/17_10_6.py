def check_item_in_list_or_dict(item, collection):
    return isinstance(collection, (list, dict)) and item in collection
if __name__ == '__main__':
    sample_list = [10, 20, 30, 'apple']
    sample_dict = {'a': 1, 'b': 2}
    test_values = ['apple', 'banana', 45]
    for value in test_values:
        exists_in_list = check_item_in_list_or_dict(value, sample_list)
        exists_in_dict = check_item_in_list_or_dict(value, sample_dict)
        print(f"Item {value}:")
        if isinstance(sample_list, list):
            result = "Found in List" if exists_in_list else "Not found in List"
        elif isinstance(sample_dict, dict):
            result = "Found in Dict" if exists_in_dict else "Not found in Dict"
        print(result)