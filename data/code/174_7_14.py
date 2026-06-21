def extract_keys(source_dict, required_keys):
    return {key: source_dict[key] for key in required_keys if key in source_dict}

if __name__ == '__main__':
    sample_dict = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York',
        'email': 'john.doe@example.com'
    }
    required_keys = ['name', 'email']
    result = extract_keys(sample_dict, required_keys)
    print(result)