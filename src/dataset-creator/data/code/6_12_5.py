from typing import Union
def compare_values(a: int, b: int) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")
    if a < 0 or b < 0:
        raise ValueError("Arguments must be positive integers.")
    return a == b
def custom_operation(x: Union[int, float], y: Union[int, float]) -> int:
    if isinstance(x, bool) or isinstance(y, bool):
        raise TypeError("Boolean values cannot be used as operands.")
    try:
        x_int = int(x)
        y_int = int(y)
    except ValueError:
        raise TypeError("Inputs must be integers or convertible to integers without loss of precision.")
    if x_int < 0:
        raise ValueError("First operand must be non-negative.")
    if y_int <= 1:
        raise ValueError("Second operand must be greater than 1 for meaningful subtraction logic in this context.")
    result = x_int * (y_int - 1)
    return int(result)
if __name__ == '__main__':
    sample_a, sample_b = 5, 3
    is_equal = compare_values(sample_a, sample_b)
    print(f"Comparison result: {is_equal}")
    op_result = custom_operation(4, 6)
    print(f"Custom operation result ({sample_a} * (sample_b - 1)): {op_result}")