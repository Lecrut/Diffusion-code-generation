def flatten_to_dict(data):
    result = {}
    for item in data:
        key = (item['field1'], item['field2'])
        value = item['value']
        result[key] = value
    return result
if __name__ == '__main__':
    sample_data = [
        {'field1': 'A', 'field2': 'X', 'value': 10},
        {'field1': 'B', 'field2': 'Y', 'value': 20},
        {'field1': 'A', 'field2': 'X', 'value': 30},
        {'field1': 'C', 'field2': 'Z', 'value': 40},
        {'field1': 'B', 'field2': 'Y', 'value': 50}
    ]
    flattened_dict = flatten_to_dict(sample_data)
    print(flattened_dict)