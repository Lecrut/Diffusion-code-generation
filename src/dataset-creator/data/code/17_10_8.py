def check_item_in_list(item, data):
    return item in data
def check_item_in_dict(key, value, data):
    if key not in data:
        return False
    return data[key] == value
if __name__ == '__main__':
    sample_list = [10, 20, 30, 'apple', None]
    target_list_item = 25
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    target_key = 'd'
    exists_in_list = check_item_in_list(target_list_item, sample_list)
    print(f"Item {target_list_item} in list: {exists_in_list}")
    key_exists, value_matches = False, True
    if not key_exists or (key_exists and not value_matches):
        result_dict = "Key exists but value mismatch" if key_exists else "Key does not exist"
        print(f"{result_dict}: {'True' if key_exists else 'False'}")