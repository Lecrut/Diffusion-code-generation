REQUIRED_KEYS = ['name', 'age', 'email']

def extract_required_keys(source_dict):
    return {key: source_dict[key] for key in REQUIRED_KEYS if key in source_dict}

if __name__ == '__main__':
    sample_data = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com',
        'address': '123 Main St'
    }
    result = extract_required_keys(sample_data)
    print(result)