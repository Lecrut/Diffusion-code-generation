def check_item_in_list(item, data):
    return item in data
def check_item_in_dict(key, value, data):
    for k, v in data.items():
        if key == k and value == v:
            return True
    return False
if __name__ == '__main__':
    sample_list = [10, 20, 30, 'apple', None]
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    target_item = 25
    found_in_list = check_item_in_list(target_item, sample_list)
    search_key = 'd'
    search_value = 4
    found_in_dict = check_item_in_dict(search_key, search_value, sample_dict)
    print(f"Item {target_item} in list: {found_in_list}")
    print(f"Key '{search_key}' and value {search_value} in dict: {found_in_dict}")