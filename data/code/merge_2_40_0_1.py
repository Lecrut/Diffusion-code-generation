def check_key_exists(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    test_keys = ['apple', 'grape', 'orange']
    for k in test_keys:
        if check_key_exists(my_dict, k):
            print(f"Key '{k}' exists.")
        else:
            print(f"Key '{k}' does not exist.")