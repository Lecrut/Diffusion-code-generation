def count_non_matching_elements(data, data_type):
    type_map = {'float': float, 'bool': bool}
    target_type = type_map.get(data_type)
    if not target_type:
        raise ValueError('Unsupported data type')
    non_matching_count = sum((1 for item in data if not isinstance(item, target_type)))
    return non_matching_count
if __name__ == '__main__':
    sample_data = [3.14, True, 'hello', 2.718]
    result = count_non_matching_elements(sample_data, 'float')
    print(result)