from typing import Union
def evaluate_parity(value: int) -> bool:
    if not isinstance(value, int):
        raise TypeError(f"Expected int, got {type(value).__name__}")
    abs_value = abs(value)
    limit = 1_000_000_000
    if abs_value > limit:
        raise ValueError(f"Value must be between -{limit} and {limit}, got {value}.")
    return value % 2 == 0
if __name__ == '__main__':
    test_cases = [1, 2, -3, 456789]
    for case in test_cases:
        try:
            result = evaluate_parity(case)
            print(f"P({case}) = {result}")
        except (TypeError, ValueError) as e:
            print(f"Error evaluating P({case}): {e}")