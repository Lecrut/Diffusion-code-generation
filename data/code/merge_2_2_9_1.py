from typing import Optional
def check_positive(value: float, epsilon: Optional[float] = None) -> bool:
    if isinstance(value, (int, float)):
        return value > -epsilon if epsilon else value > 0
    raise TypeError("Input must be an integer or float.")
if __name__ == '__main__':
    sample_values = [1.5, 0.0, -2.3]
    thresholds = [None, 1e-9]
    for val in sample_values:
        result_default = check_positive(val)
        print(f"Value {val} is positive (default): {result_default}")
        if len(thresholds) > 0 and isinstance(result_default, bool):
            epsilon_val = thresholds[0]
            result_custom = check_positive(val, epsilon=epsilon_val)
            print(f"Value {val} is positive (threshold={epsilon_val}): {result_custom}")