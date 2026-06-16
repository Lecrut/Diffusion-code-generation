import sys
from collections import OrderedDict
def is_item_in_list(items: list, target) -> bool:
    return target in items
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    test_cases = [5, 30, 99]
    for item in test_cases:
        result = is_item_in_list(sample_data, item)
        print(f"{item}: {result}")