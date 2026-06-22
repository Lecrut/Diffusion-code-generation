def extract_and_flatten(data):
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("Input must be a list of dictionaries")
    
    result = []
    for d in data:
        if 'key1' in d and 'key2' in d:
            result.append((d['key1'], d['key2']))
    
    return result

if __name__ == '__main__':
    sample_data = [{'key1': 1, 'key2': 5}, {'key1': 3, 'key2': 8}, {'key1': 7, 'key2': 2}, {'key1': 4, 'key2': 9}]
    try:
        result = extract_and_flatten(sample_data)
        print(result)
    except ValueError as e:
        print(e)