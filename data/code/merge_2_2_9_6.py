from typing import Optional
def check_positive(value: float, epsilon: Optional[float] = None) -> bool:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value > 0.0
    raise TypeError("The 'value' argument must be a number.")
if __name__ == '__main__':
    sample_values = [1.5, -3.2, 0.0, 4e-9]
    test_cases = [
        (sample_values[0], None),
        (sample_values[1], None),
        (sample_values[2], None),
        (sample_values[3], 1e-8)
    ]
    for val, eps in test_cases:
        result = check_positive(val, epsilon=eps)
        print(f"check_positive({val}, {eps}) is {result}")