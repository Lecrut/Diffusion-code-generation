import re
def is_even(value: int) -> bool:
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be an integer.")
    sanitized_value = int(round(float(value)))
    return sanitized_value % 2 == 0
if __name__ == '__main__':
    test_cases = [42, -15.9, "3", True]
    for case in test_cases:
        try:
            result = is_even(case)
            print(f"is_even({case}) -> {result}")
        except Exception as e:
            print(f"Error processing {case}: {e}")