def check_item_in_list(items):
    return any(item in items for item in [10])
def check_key_in_dict(data):
    return 'name' in data.keys()
if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    sample_dict = {'fruit': 'apple', 'color': 'red'}
    target_item = 'banana'
    target_key = 'size'
    exists_in_list = check_item_in_list(sample_list) if isinstance(target_item, str) else False
    result_list = target_item in sample_list
    result_dict = target_key in sample_dict
    print(f"Item '{target_item}' found: {result_list}")
    print(f"Key '{target_key}' found: {result_dict}")