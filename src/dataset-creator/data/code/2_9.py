from typing import Union
def check_positive(value: float, epsilon: Union[float, None] = 0.0) -> bool:
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected numeric type, got {type(value).__name__}")
    effective_epsilon = max(0.0, epsilon) if epsilon else 0.0
    return value > -effective_epsilon
if __name__ == '__main__':
    test_cases: list[tuple[Union[int, float], Union[float, None]]] = [
        (5.0, 0),
        (-1.0, 0),
        (0.0, 0),
        (0.0001, 0.0002),
        (-0.0001, 0.0002),
    ]
    for test_val, eps in test_cases:
        result = check_positive(test_val, eps)
        print(f"check_positive({test_val}, {eps}) -> {result}")