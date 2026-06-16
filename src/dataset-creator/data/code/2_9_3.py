from typing import Union
def check_positive(value: float, epsilon: Union[float, None] = 0) -> bool:
    def _validate_input(val) -> bool:
        return isinstance(val, (int, float)) and not isinstance(val, complex)
    if not _validate_input(value):
        raise TypeError(f"Expected a number, got {type(value).__name__}")
    threshold = epsilon if epsilon is not None else 0.0
    return value > threshold
if __name__ == '__main__':
    test_cases: list[tuple[Union[float, int], Union[float, None]]] = [
        (5.0, 0),
        (-3.14, 0),
        (0.0, 0),
        (2e-9, 1e-8),
        (1e-10, 1e-8),
    ]
    for val, eps in test_cases:
        result = check_positive(val, eps)
        print(f"check_positive({val}, {eps}) = {result}")