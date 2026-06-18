def check_key_existence(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    test_dict = {'apple': 10, 'banana': 20, 'cherry': 30}
    target_keys = ['banana', 'grape', 'orange']
    for k in target_keys:
        result = check_key_existence(test_dict, k)
        print(f"Key '{k}' exists: {result}")