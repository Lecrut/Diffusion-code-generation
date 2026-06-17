def contains_key(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    test_data = {'apple': 10, 'banana': 20}
    print(contains_key(test_data, 'orange'))
    print(contains_key(test_data, 'banana'))