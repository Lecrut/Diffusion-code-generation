def flatten_to_dict(data):
    result = {}
    for item in data:
        key = (item['field1'], item['field2'])
        value = item['value']
        result[key] = value
    return result
if __name__ == '__main__':
    sample_list = [
        {'field1': 'A', 'field2': 'X', 'value': 100},
        {'field1': 'B', 'field2': 'Y', 'value': 200},
        {'field1': 'A', 'field2': 'X', 'value': 150},
        {'field1': 'C', 'field2': 'Z', 'value': 300},
        {'field1': 'B', 'field2': 'Y', 'value': 250}
    ]
    flattened_dict = flatten_to_dict(sample_list)
    print(flattened_dict)