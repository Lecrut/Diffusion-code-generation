def find_by_value(data_dict: dict, target):
    if not isinstance(data_dict, dict):
        raise TypeError("The first argument must be a dictionary.")
    for key in data_dict:
        if data_dict[key] == target:
            return str(key)
    return None
def contains_key(data_dict: dict, search_key):
    if not isinstance(data_dict, dict):
        raise TypeError("The first argument must be a dictionary.")
    return search_key in data_dict
if __name__ == '__main__':
    sample_data = {
        'user_id_001': {'role': 'admin', 'status': 'active'},
        'user_id_002': {'role': 'editor', 'status': 'inactive'},
        'user_id_003': {'role': 'viewer', 'status': 'active'}
    }
    target_role = 'admin'
    found_key = None
    if sample_data:
        for key, val in sample_data.items():
            if isinstance(val.get('role'), str):
                if find_by_value(sample_data, {'role': target_role}): 
                    print(f"Key with role '{target_role}' found: {found_key}")
    simple_map = {'apple': 'red', 'banana': 'yellow'}
    result_key = find_by_value(simple_map, 'red')
    print(f"Key for value 'red' is: {result_key}")
    test_keys = ['orange', 'banana']
    for k in test_keys:
        exists = contains_key(simple_map, k)
        status = "Exists" if exists else "Does not exist"
        print(f"Key '{k}' {status}")
    try:
        invalid_input = [1, 2, 3]
        find_by_value(invalid_input, 'target')
    except TypeError as e:
        print(f"Caught expected error for non-dict input: {e}")