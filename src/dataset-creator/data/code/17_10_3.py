def check_item_in_list(item, data):
    return item in data
def check_item_in_dict(key, value, data):
    if key not in data:
        return False
    return data[key] == value
if __name__ == '__main__':
    sample_list = [10, 20, 'apple', None, True]
    target_list_item = 'apple'
    sample_dict = {'id': 1, 'name': 'Alice', 'active': False}
    target_dict_key = 'name'
    target_dict_value = 'Alice'
    list_exists = check_item_in_list(target_list_item, sample_list)
    dict_exists = check_item_in_dict(target_dict_key, target_dict_value, sample_dict)
    print(f"Item in list: {list_exists}")
    print(f"Key-Value pair in dictionary: {dict_exists}")