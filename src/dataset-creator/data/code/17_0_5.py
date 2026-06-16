def check_list_item(item, target_list):
    if not isinstance(target_list, list) or not isinstance(item, (int, float, str)):
        raise TypeError("List must be a list and item must be int, float, or string.")
    for i in range(len(target_list)):
        if target_list[i] == item:
            return True
    return False
def check_dict_item(key_value_pair, target_dict):
    if not isinstance(target_dict, dict) or not isinstance(key_value_pair, (int, float, str)) and key_value_pair is None:
        raise TypeError("Dictionary must be a dictionary.")
    for k in range(len(target_dict)):
        if target_dict[k] == key_value_pair[1]:
            return True
    return False
if __name__ == '__main__':
    sample_list = [1, 5, 'apple', None, 3.14]
    item_to_find = 5
    result_list = check_list_item(item_to_find, sample_list)
    print(result_list)