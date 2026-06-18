def check_key_presence(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    test_dict = {'apple': 1, 'banana': 2}
    print(check_key_presence(test_dict, 'orange'))