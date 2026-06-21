def extract_keys(source_dict, required_keys):
    return {key: source_dict[key] for key in required_keys if key in source_dict}

if __name__ == '__main__':
    sample_dict = {
        'name': 'Alice',
        'age': 25,
        'city': 'Wonderland',
        'occupation': 'Queen'
    }
    keys_to_extract = ['name', 'age']
    result = extract_keys(sample_dict, keys_to_extract)
    print(result)