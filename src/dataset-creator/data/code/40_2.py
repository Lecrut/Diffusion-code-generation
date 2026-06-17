def check_key_exists(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    test_data = {'apple': 10, 'banana': 20}
    print(check_key_exists(test_data, 'orange'))