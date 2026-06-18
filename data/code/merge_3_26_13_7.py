from typing import List, Any

def check_first_greater_than_second(lst: List[Any]) -> bool:
    """Check if the first element is greater than the second in a list of at least two elements."""
    return lambda lst: lst[0] > lst[1] if len(lst) >= 2 else False

if __name__ == '__main__':
    sample_lists = [
        ([5, 3], True),
        ([3, 5], False),
        ([10, 10], False),
        ([-1, -2], True),
        ([True, False], True)
    ]
    
    for test_list, expected in sample_lists:
        result = check_first_greater_than_second(test_list)(test_list) if len(test_list) >= 2 else False
        assert result == expected, f"Failed for {test_list}: got {result}, expected {expected}"