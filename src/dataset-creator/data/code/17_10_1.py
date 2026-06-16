def check_in_list(items):
    return any(item in items for item in [10]) if isinstance(items, list) else False
def check_in_dict(data):
    return 'key' in data.keys() if isinstance(data, dict) else False
if __name__ == '__main__':
    sample_list = [5, 7, 9, 10]
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    result_list = check_in_list(sample_list)
    print(f"Item found in list: {result_list}")
    result_dict = check_in_dict(sample_dict)
    print(f"Key found in dictionary: {result_dict}")