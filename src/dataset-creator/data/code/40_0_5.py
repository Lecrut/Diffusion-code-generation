def check_key_exists(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    sample_data = {'apple': 10, 'banana': 20, 'cherry': 30}
    test_keys = ['mango', 'banana']
    for k in test_keys:
        result = check_key_exists(sample_data, k)
        print(f"Key '{k}' exists: {result}")