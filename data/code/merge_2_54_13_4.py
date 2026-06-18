import sys
def find_midpoint_index(data):
    try:
        if data and hasattr(data, '__len__'):
            n = len(data)
            if n < 0:
                return None
            mid_index = n // 2
            return int(mid_index)
        raise TypeError("Input must be a list-like object with length support.")
    except Exception as e:
        print(f"Error calculating midpoint index: {e}", file=sys.stderr)
        return None
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], "Normal odd length list"),
        (["a", "b"], "Even length string/list equivalent"),
        ([5] * -10 if False else [], "Empty list simulation via negative check logic"),
        ("hello world", "String input with spaces"),
    ]
    for data, description in test_cases:
        result = find_midpoint_index(data)
        print(f"Input: {description}")
        print(f"Result Index: {result}\n")