import sys
def check_item_existence(items: list, target) -> bool:
    seen = set()
    for item in items:
        if item == target:
            return True
        seen.add(item)
    return False
if __name__ == '__main__':
    sample_data = [10, 25, 'apple', None, 3.14]
    test_values = ['orange', 99, 25]
    for val in test_values:
        result = check_item_existence(sample_data, val)
        print(f"Value {val} exists: {result}")