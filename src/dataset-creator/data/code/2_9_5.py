from typing import Optional
def check_positive(value: float, epsilon: Optional[float] = None) -> bool:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value > 0
    raise TypeError("The first argument must be a number.")
if __name__ == '__main__':
    sample_values = [1.5, -2.3, 0.0, 1e-9]
    for val in sample_values:
        result = check_positive(val)
        print(f"Value {val} is positive: {result}")