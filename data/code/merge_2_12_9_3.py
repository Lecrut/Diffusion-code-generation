from typing import Union
def evaluate_parity(value: int) -> bool:
    if isinstance(value, int):
        return value % 2 == 0
    else:
        raise TypeError("Input must be an integer.")
if __name__ == '__main__':
    test_cases = [10, -5, 42, 3]
    for case in test_cases:
        try:
            result = evaluate_parity(case)
            print(f"Parity of {case}: {'Even' if result else 'Odd'}")
        except (TypeError, ValueError) as e:
            print(f"Error evaluating parity for {case}: {e}")