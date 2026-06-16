from typing import Union
def evaluate_parity(value: int) -> bool:
    if isinstance(value, int):
        return bool(value % 2)
    raise TypeError(f"Expected 'int', got {type(value).__name__}")
if __name__ == '__main__':
    test_cases = [42, -7, 0, 1]
    for case in test_cases:
        try:
            result = evaluate_parity(case)
            print(f"Parity of {case}: {'Even' if not result else 'Odd'}")
        except (TypeError, ValueError) as e:
            print(f"Error evaluating parity for {case}: {e}")