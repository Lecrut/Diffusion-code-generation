def check_key_exists(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    sample_dict = {'apple': 10, 'banana': 20, 'cherry': 30}
    test_keys = ['mango', 'banana', None]
    for k in test_keys:
        result = check_key_exists(sample_dict, k)
        print(f"Key '{k}' exists: {result}")