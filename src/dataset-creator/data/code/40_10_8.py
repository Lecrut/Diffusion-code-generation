def check_key_exists(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    test_dict = {'apple': 10, 'banana': 20, 'cherry': 30}
    sample_keys = ['mango', 'orange']
    for k in sample_keys:
        result = check_key_exists(test_dict, k)
        print(f"Key '{k}' exists: {result}")