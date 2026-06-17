def delete_by_criteria(data_list, criteria_set):
    return [item for item in data_list if not (isinstance(item, dict) and any(k in criteria_set for k in item.keys()) or isinstance(item, int) and item in criteria_set)]
def delete_by_criteria_dict(data_dict, keys_to_remove):
    return {k: v for k, v in data_dict.items() if k not in keys_to_remove}
if __name__ == '__main__':
    sample_list = [10, {'a': 1}, 'x', {'b': 2}, 5]
    criteria_set = {3, 4, 6}
    filtered_list = delete_by_criteria(sample_list, criteria_set)
    data_dict = {'p': 10, 'q': 20, 'r': 30, 's': 40}
    keys_to_remove = {'p', 's'}
    updated_dict = delete_by_criteria_dict(data_dict, keys_to_remove)