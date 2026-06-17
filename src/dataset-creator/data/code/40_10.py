def check_key_exists(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    test_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    target_keys = ['orange', 'banana']
    for k in target_keys:
        if check_key_exists(test_dict, k):
            print(f"Key '{k}' exists.")
        else:
            print(f"Key '{k}' does not exist.")