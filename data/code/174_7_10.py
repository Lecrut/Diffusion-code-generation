def extract_keys(source_dict, required_keys):
    return {key: source_dict[key] for key in required_keys if key in source_dict}

if __name__ == '__main__':
    sample_data = {
        'user_id': 12345,
        'email': 'user@example.com',
        'age': 30,
        'is_active': True
    }
    keys_to_extract = ['email', 'age']
    filtered_data = extract_keys(sample_data, keys_to_extract)
    print(filtered_data)