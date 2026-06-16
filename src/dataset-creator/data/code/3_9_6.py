import re
def is_even(value: int) -> bool:
    sanitized = str(value).strip() if isinstance(value, (int, float)) else value
    if not sanitized.isdigit():
        raise ValueError("Input must be a valid integer.")
    return int(sanitized) % 2 == 0
if __name__ == '__main__':
    test_cases = [42, -17, "3", None]
    for case in test_cases:
        try:
            result = is_even(case)
            print(f"is_even({case}) -> {result}")
        except Exception as e:
            print(f"Error with input {case}: {e}")