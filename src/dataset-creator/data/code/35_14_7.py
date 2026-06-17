def find_by_value(data: dict, target_value):
    if not isinstance(data, dict):
        raise TypeError("The first argument must be a dictionary.")
    for key in data.keys():
        value = data[key]
        if value == target_value:
            return (key, value)
    return None
def find_by_key_exists(data: dict, required_keys):
    if not isinstance(data, dict):
        raise TypeError("The first argument must be a dictionary.")
    result_dict = {}
    for key in required_keys:
        if key in data:
            result_dict[key] = data[key]
    return result_dict
def find_by_predicate(data: dict, predicate):
    if not isinstance(data, dict):
        raise TypeError("The first argument must be a dictionary.")
    matches = []
    for key in data.keys():
        value = data[key]
        item_tuple = (key, value)
        try:
            result = predicate(item_tuple)
            if result is True or result == 1:                                                  
                matches.append(item_tuple)
        except Exception as e:
            raise RuntimeError(f"Predicate function raised an exception for item {item_tuple}: {e}")
    return matches
if __name__ == '__main__':
    sample_data = {'id_01': 'Alice', 'id_02': 'Bob', 'id_03': 'Charlie'}
    target_name = "Alice"
    result_key, result_val = find_by_value(sample_data, target_name)
    print(f"Found key: {result_key}, value: {result_val}")
    required_ids = ['id_01', 'nonexistent']
    filtered_result = find_by_key_exists(sample_data, required_ids)
    print(f"Filtered keys result: {filtered_result}")
    def is_name_length_greater_than_four(item):
        return len(item[1]) > 4
    predicate_matches = find_by_predicate(sample_data, is_name_length_greater_than_four)
    for match in predicate_matches:
        print(f"Match found: {match}")