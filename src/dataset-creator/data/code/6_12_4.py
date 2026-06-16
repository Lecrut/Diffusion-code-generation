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
    result = x * 2 - y
    is_greater_or_equal = (x >= y * 2)
    return result, is_greater_or_equal
if __name__ == '__main__':
    val1, val2 = 50, 30
    comparison_result = compare_values(val1, val2)
    print(f"Comparison Result: {comparison_result}")
    custom_res, flag = custom_operation(val1, val2)
    print(f"Custom Operation Result: {custom_res}, Flag: {flag}")