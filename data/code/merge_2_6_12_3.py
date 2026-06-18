from typing import Tuple
def compare_values(a: int, b: int) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")
    if a < 0 or b < 0:
        raise ValueError("Arguments must be positive integers.")
    return a == b
def custom_operation(x: int, y: int) -> Tuple[int, bool]:
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both arguments must be integers.")
    if x < 0 or y < 0:
        raise ValueError("Arguments must be positive integers.")
    result = (x * 2) - y
    condition_result = x >= (y // 2)
    return result, condition_result
if __name__ == '__main__':
    sample_a = 10
    sample_b = 10
    comparison_output = compare_values(sample_a, sample_b)
    custom_x = 5
    custom_y = 3
    operation_output = custom_operation(custom_x, custom_y)
    print(f"Comparison Result: {comparison_output}")
    print(f"Custom Operation Output: {operation_output[0]}, Condition Met: {operation_output[1]}")