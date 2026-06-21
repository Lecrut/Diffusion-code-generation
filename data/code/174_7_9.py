def extract_keys(source_dict, required_keys):
    return {key: source_dict[key] for key in required_keys if key in source_dict}

if __name__ == '__main__':
    sample_dict = {
        'name': 'John',
        'age': 30,
        'city': 'New York',
        'email': 'john@example.com'
    }
    keys_to_extract = ['name', 'email']
    result = extract_keys(sample_dict, keys_to_extract)
    print(result)