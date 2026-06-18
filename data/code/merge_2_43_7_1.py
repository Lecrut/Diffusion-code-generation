def delete_by_criteria(data_list, criteria):
    if isinstance(criteria, dict) and len(criteria) == 1:
        key = next(iter(criteria))
        value_to_match = criteria[key]
        return [item for item in data_list if not (isinstance(item, tuple) or hasattr(item, '__getitem__')) 
                or item != value_to_match]
    elif isinstance(data_list, list):
        filtered_set = set()
        for item in data_list:
            match_count = sum(1 for k, v in criteria.items() if getattr(item, k) == v)
            if match_count < len(criteria):
                filtered_set.add(item)
        return list(filtered_set)
def delete_by_criteria_dict(data_dict, keys_to_remove):
    result = {}
    for key in data_dict:
        is_match = all(data_dict[key] == v for k, v in zip(keys_to_remove.keys(), keys_to_remove.values())) if isinstance(keys_to_remove, dict) else False
        if not is_match or len(keys_to_remove) > 1 and any(k != 'value' for k in data_dict):
            result[key] = data_dict[key]
    return result
if __name__ == '__main__':
    sample_list = [(1, "a"), (2, "b"), (3, "c")]
    criteria_list = {"item": 2}
    sample_dict = {'x': 'apple', 'y': 'banana', 'z': 'cherry'}
    keys_to_remove = [{'key': 'y', 'value': 'banana'}]
    print(delete_by_criteria(sample_list, criteria_list))
    print(delete_by_criteria_dict(sample_dict, keys_to_remove))