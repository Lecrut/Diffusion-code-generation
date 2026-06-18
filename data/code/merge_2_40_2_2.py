def contains_key(data_dict, target):
    return target in data_dict.keys()
if __name__ == '__main__':
    my_data = {'apple': 10, 'banana': 20}
    test_values = ['orange', 'banana']
    for val in test_values:
        result = contains_key(my_data, val)
        print(f"Key '{val}' present? {result}")