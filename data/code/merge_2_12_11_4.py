from typing import Union
def check_parity(value: int) -> bool:
    if isinstance(value, (int, float)):
        return value % 2 == 0
    raise TypeError(f"Expected integer or valid number, got {type(value).__name__}")
if __name__ == '__main__':
    test_cases = [10, -5, 42.7, "seven", None]
    for case in test_cases:
        try:
            result = check_parity(case)
            print(f"Parity of {case}: {result}")
        except (TypeError, ValueError) as e:
            print(f"Error checking parity for {case}: {e}")