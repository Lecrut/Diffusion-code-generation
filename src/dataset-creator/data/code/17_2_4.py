import sys
def check_item_existence(data_list: list, target) -> bool:
    return target in data_list
if __name__ == '__main__':
    sample_data = [10, 25, 'apple', None, True]
    test_values = ['banana', 10, None, False]
    for val in test_values:
        exists = check_item_existence(sample_data, val)
        print(f"Is {val} present? {exists}")