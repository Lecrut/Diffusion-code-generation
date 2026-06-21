def extract_keys(source_dict, required_keys):
    filtered_dict = {}
    for key in required_keys:
        if key in source_dict:
            filtered_dict[key] = source_dict[key]
    return filtered_dict

if __name__ == '__main__':
    sample_data = {
        'username': 'john_doe',
        'email': 'john@example.com',
        'age': 30,
        'address': '123 Main St'
    }
    keys_to_extract = ['username', 'email']
    result = extract_keys(sample_data, keys_to_extract)
    print(result)