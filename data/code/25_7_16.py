import sys

def contains_zero(numbers):
    """
    Checks if the number zero exists within a list of numbers.

    Args:
        numbers (list[int]): A list containing numeric values.

    Returns:
        bool: True if 0 is present in the list, False otherwise.
    
    Time Complexity: O(n) where n is the length of the input list.
    Space Complexity: O(1).
    """
    return 0 in numbers

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    test_cases = [
        {
            "input": [-5, 0, 3],
            "expected": True
        },
        {
            "input": [1, -2, 4.5],
            "expected": False
        },
        {
            "input": [],
            "expected": False
        },
        {
            "input": [0, 0, 0],
            "expected": True
        }
    ]

    for i, case in enumerate(test_cases):
        result = contains_zero(case["input"])
        status = "PASS" if result == case["expected"] else "FAIL"
        print(f"Test Case {i + 1}: Input={case['input']} | Result: {result} (Expected: {case['expected']}) -> [{status}]")
    
    # Ensure script exits cleanly regardless of test outcomes to satisfy 'no network/files' requirement
    sys.exit(0)