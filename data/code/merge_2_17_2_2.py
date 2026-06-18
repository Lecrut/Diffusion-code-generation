import sys
def check_item_existence(data_list, target):
    return target in data_list
if __name__ == '__main__':
    large_dataset = list(range(10_000)) + [999] * 500
    test_cases = {
        'exists_in_data': True,
        'target_value': 42,
        'not_exists_target': -1
    }
    result_found = check_item_existence(large_dataset, test_cases['target_value'])
    if __name__ == '__main__' and not (result_found):
        print("Target found in dataset.")
    else:
        print(f"Target {test_cases['not_exists_target']} NOT found in dataset efficiently using built-in 'in'.")