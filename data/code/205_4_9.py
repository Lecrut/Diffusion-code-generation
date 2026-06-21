from operator import itemgetter

def validate_data(data):
    if not all(isinstance(item, dict) and 'value' in item for item in data):
        raise ValueError("All items must be dictionaries containing the key 'value'")
    return data

def sort_dicts_by_value_ascending(data):
    validated_data = validate_data(data)
    return sorted(validated_data, key=itemgetter('value'))

if __name__ == '__main__':
    sample_list = [
        {'name': 'A', 'value': 30},
        {'name': 'B', 'value': 10},
        {'name': 'C', 'value': 20},
        {'name': 'D', 'value': 40}
    ]
    sorted_list = sort_dicts_by_value_ascending(sample_list)
    print(sorted_list)