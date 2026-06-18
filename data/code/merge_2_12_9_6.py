from typing import Union
def evaluate_parity(value: int) -> bool:
    if not isinstance(value, int):
        raise TypeError(f"Expected int, got {type(value).__name__}")
    if value > 100 or value < -50:
        raise ValueError("Value must be between -50 and 100 inclusive.")
    return value % 2 == 0
if __name__ == '__main__':
    test_cases = [4, 7, 0, -3]
    for case in test_cases:
        try:
            result = evaluate_parity(case)
            print(f"P({case}) = {result}")
        except (TypeError, ValueError) as e:
            print(f"Error evaluating P({case}): {e}")