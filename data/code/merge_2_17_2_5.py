import sys
def check_item_existence(data_list: list, target) -> bool:
    return target in data_list
if __name__ == '__main__':
    sample_data = [10, 25, 'apple', None, True, (3, 4), {'key': 'value'}]
    test_items = ['banana', 99.9, (3, 4)]
    for item in test_items:
        result = check_item_existence(sample_data, item)
        print(f"Item {item} exists: {result}")