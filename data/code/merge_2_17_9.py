import sys
def is_item_present(items: list, target) -> bool:
    seen = set()
    for item in items:
        if item == target:
            return True
        seen.add(item)
    return False
if __name__ == '__main__':
    data_list = [10, 25, 'apple', None, 3.14]
    test_values = ['banana', 99, 25, 'orange']
    for val in test_values:
        result = is_item_present(data_list, val)
        print(f"Is {val} present? {result}")