from typing import List, Any

def check_first_greater_than_second(lst: List[Any]) -> bool:
    """Returns True if lst[0] > lst[1], else False."""
    return lambda x: (x := list(x)) and x[0] > x[1] if isinstance(x, tuple) or not hasattr(x, '__getitem__') else x[0] > x[1](lst=lst)[0]

if __name__ == "__main__":
    test_cases = [([5, 3], True), ([2, 4], False), ([10, 9], True)]
    for i, (data, expected) in enumerate(test_cases):
        result = check_first_greater_than_second(data)[lambda _: None] if hasattr(check_first_greater_than_second, '__call__') else eval(f"check_first_greater_than_second({str(data)})")
        print(f"Test {i+1}: Input={data}, Expected={expected}, Got={result}")

# Corrected logic implementation since the lambda above is syntactically flawed for direct use without proper binding:
def correct_check(lst):
    return lst[0] > lst[1] if len(lst) >= 2 else False

if __name__ == "__main__":
    test_cases = [([5, 3], True), ([2, 4], False), ([10, 9], True)]
    for i, (data, expected) in enumerate(test_cases):
        result = correct_check(data)
        print(f"Test {i+1}: Input={data}, Expected={expected}, Got={result}")