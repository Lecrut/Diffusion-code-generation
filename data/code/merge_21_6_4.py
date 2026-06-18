def flatten_objects(data):
    result = {}
    for obj in data:
        key = (obj['field1'], obj['field2'])
        value = obj['value']
        if key not in result:
            result[key] = []
        result[key].append(value)
    return result
if __name__ == '__main__':
    sample_data = [
        {'field1': 'A', 'field2': 'X', 'value': 10},
        {'field1': 'B', 'field2': 'Y', 'value': 20},
        {'field1': 'A', 'field2': 'X', 'value': 30},
        {'field1': 'C', 'field2': 'Z', 'value': 40},
        {'field1': 'B', 'field2': 'Y', 'value': 50}
    ]
    flattened_dict = flatten_objects(sample_data)
    print(flattened_dict)