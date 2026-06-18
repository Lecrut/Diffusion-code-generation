from typing import Union
def evaluate_parity(value: int) -> bool:
    if not isinstance(value, int):
        raise TypeError(f"Expected int, got {type(value).__name__}")
    min_limit = -10**9
    max_limit = 10**9
    if value < min_limit or value > max_limit:
        raise ValueError(f"value must be between {min_limit} and {max_limit}, got {value}")
    return value % 2 == 0
if __name__ == '__main__':
    test_cases = [1, -5, 42, 0]
    for case in test_cases:
        result = evaluate_parity(case)
        print(f"P({case}) = {result}")