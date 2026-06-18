from typing import Tuple
def compare_values(a: int, b: int) -> bool:
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers.")
    return a == b
def custom_operation(a: int, b: int) -> Tuple[int, bool]:
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers.")
    diff = a - b
    result_metric = diff * 2
    return result_metric, (a >= b)
if __name__ == '__main__':
    sample_a = 15
    sample_b = 7
    comparison_result = compare_values(sample_a, sample_b)
    custom_res, is_greater_equal = custom_operation(sample_a, sample_b)
    print(f"Comparison Result: {comparison_result}")
    print(f"Custom Operation Metric: {custom_res}, Is Greater or Equal: {is_greater_equal}")