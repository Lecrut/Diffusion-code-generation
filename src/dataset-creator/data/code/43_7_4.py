def delete_by_criteria(data_list, criteria):
    if isinstance(criteria, dict) and 'value' in criteria:
        target_values = {criteria['value']}
        return [item for item in data_list if item not in target_values]
def delete_by_criteria_dict(data_dict, keys_to_delete):
    if isinstance(keys_to_delete, list) and len(keys_to_delete) > 0:
        new_data = {}
        for k, v in data_dict.items():
            if not any(k == x or (isinstance(x, dict) and set(v.keys()) & {x.get('key', '')}) for x in keys_to_delete):
                new_data[k] = v
    return new_data
if __name__ == '__main__':
    sample_list = [10, 20, 30, 'apple', 'banana']
    criteria_value = 20
    result_list = delete_by_criteria(sample_list, {'value': criteria_value})
    print("Filtered List:", result_list)
    sample_dict = {
        "id_1": {"name": "Alice", "age": 30},
        "id_2": {"name": "Bob", "age": 25},
        "id_3": {"name": "Charlie", "age": 40}
    }
    keys_to_delete = ["id_1"]
    result_dict = delete_by_criteria_dict(sample_dict, keys_to_delete)
    print("Filtered Dictionary:", result_dict)