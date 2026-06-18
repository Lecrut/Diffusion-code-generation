def check_key_exists(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    test_data = {'apple': 10, 'banana': 20, 'cherry': 30}
    target_keys = ['mango', 'banana']
    for k in target_keys:
        result = check_key_exists(test_data, k)
        print(f"Key '{k}' exists: {result}")