from typing import Union
def evaluate_parity(value: int) -> bool:
    if isinstance(value, int):
        return value % 2 == 0
    raise TypeError(f"Expected int, got {type(value).__name__}")
if __name__ == '__main__':
    test_cases = [10, -5, 0]
    for case in test_cases:
        try:
            result = evaluate_parity(case)
            print(f"P({case}) = {result}")
        except TypeError as e:
            print(f"Error evaluating P({case}): {e}")