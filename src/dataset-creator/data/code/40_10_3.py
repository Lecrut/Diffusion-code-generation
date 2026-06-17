def check_key_exists(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    test_dict = {'apple': 10, 'banana': 20}
    target_key = 'orange'
    result = check_key_exists(test_dict, target_key)
    if result:
        print(f"Key '{target_key}' exists.")
    else:
        print(f"Key '{target_key}' does not exist.")