def extract_keys(source_dict, required_keys):
    filtered_dict = {}
    for key in required_keys:
        if key in source_dict:
            filtered_dict[key] = source_dict[key]
    return filtered_dict

if __name__ == '__main__':
    sample_data = {
        'user_id': 12345,
        'username': 'john_doe',
        'email': 'john.doe@example.com',
        'age': 30
    }
    keys_to_extract = ['user_id', 'email']
    result = extract_keys(sample_data, keys_to_extract)
    print(result)