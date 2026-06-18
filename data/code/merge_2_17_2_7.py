import sys
def check_item_existence(items: list, target) -> bool:
    return target in items
if __name__ == '__main__':
    sample_data = [10, 25, 'apple', None, True]
    test_cases = [
        ('apple', True),
        (42, False),
        (None, True)
    ]
    for item, expected in test_cases:
        result = check_item_existence(sample_data, item)
        if not isinstance(result, bool):
            print(f"Error: Result is not a boolean")
        elif result != expected:
            print(f"Test failed for {item}: Expected {expected}, got {result}")
            sys.exit(1)
        else:
            continue
    print("All tests passed.")