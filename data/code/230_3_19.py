def extract_and_flatten(data):
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("All items in the list must be dictionaries.")
    
    return [item['key'] for item in data]

if __name__ == '__main__':
    sample_data = [{'key': 1}, {'key': 3}, {'key': 7}, {'key': 4}]
    result = extract_and_flatten(sample_data)
    print(result)