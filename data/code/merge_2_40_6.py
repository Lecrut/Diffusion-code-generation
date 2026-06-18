def check_key_presence(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    sample_data = {'apple': 1, 'banana': 2}
    test_keys = ['apple', 'cherry']
    for k in test_keys:
        print(f"Key '{k}' present: {check_key_presence(sample_data, k)}")