def delete_by_criteria(data_list, criteria):
    if isinstance(criteria, dict) and len(criteria) == 1:
        key = next(iter(criteria))
        value = criteria[key]
        target_indices = {i for i in range(len(data_list)) 
                        if data_list[i].get(key) == value}
        return [item for idx, item in enumerate(data_list) if idx not in target_indices]
    else:
        raise ValueError("Criteria must be a dictionary with exactly one key-value pair.")
def delete_by_criteria_dict(dictionary_data, criteria):
    if isinstance(criteria, dict) and len(criteria) == 1:
        key = next(iter(criteria))
        value = criteria[key]
        target_keys = {k for k in dictionary_data.keys() 
                      if dictionary_data[k].get(key) == value}
        return {k: v for k, v in dictionary_data.items() if k not in target_keys}
    else:
        raise ValueError("Criteria must be a dictionary with exactly one key-value pair.")
if __name__ == '__main__':
    sample_list = [
        {'id': 101, 'status': 'active'},
        {'id': 102, 'status': 'inactive'},
        {'id': 103, 'status': 'active'},
        {'id': 104, 'status': 'pending'}
    ]
    sample_dict = {
        'user_1': {'name': 'Alice', 'role': 'admin'},
        'user_2': {'name': 'Bob', 'role': 'editor'},
        'user_3': {'name': 'Charlie', 'role': 'admin'}
    }
    criteria_list = {'status': 'inactive'}
    filtered_list = delete_by_criteria(sample_list, criteria_list)
    criteria_dict = {'role': 'admin'}
    filtered_dict = delete_by_criteria_dict(sample_dict, criteria_dict)
    print("Filtered List:", filtered_list)
    print("Filtered Dict:", filtered_dict)