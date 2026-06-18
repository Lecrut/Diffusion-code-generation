import sys
def check_item_existence(data_list: list, target_value) -> bool:
    if not data_list:
        return False
    unique_items = set(data_list)
    return target_value in unique_items
if __name__ == '__main__':
    sample_data = [1, 2, 3, 'a', 'b', None] * 10**5
    test_cases = [
        (42, False),
        ('a', True),
        (None, True),
        (-999, False)
    ]
    for value, expected in test_cases:
        result = check_item_existence(sample_data, value)
        assert result == expected, f"Test failed for {value}: got {result}, expected {expected}"
    print("All tests passed.")