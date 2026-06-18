def check_item_in_list(item, data):
    return item in data
def check_item_in_dict(key_or_value, data):
    if isinstance(key_or_value, tuple) and len(key_or_value) == 2:
        key, value = key_or_value
        return (key in data) and (data[key] == value)
    elif isinstance(key_or_value, str):
        for k, v in data.items():
            if str(k) == str(key_or_value) or str(v) == str(key_or_value):
                return True
        return False
    else:
        key = key_or_value
        return key in data
if __name__ == '__main__':
    sample_list = [1, 2, 'apple', None]
    target_item = 'apple'
    sample_dict = {'a': 1, 'b': 2}
    search_tuple = ('a', 1)
    string_search = "A"
    exists_in_list = check_item_in_list(target_item, sample_list)
    print(f"Item '{target_item}' in list: {exists_in_list}")
    found_by_key_val = check_item_in_dict(search_tuple, sample_dict)
    print(f"Key-value pair ({search_tuple[0]}, {search_tuple[1]}) in dict: {found_by_key_val}")
    found_by_string = check_item_in_dict(string_search, sample_dict)
    print(f"String '{string_search}' in dict keys/values (case-insensitive): {found_by_string}")