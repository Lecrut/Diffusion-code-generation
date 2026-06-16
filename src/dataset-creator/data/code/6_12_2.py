from typing import Tuple
def compare_values(a: int, b: int) -> bool:
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers.")
    return a == b
def custom_calculation(a: int, multiplier: int) -> Tuple[int, bool]:
    if a <= 0 or multiplier <= 0:
        raise ValueError("Inputs must be positive integers.")
    product = a * multiplier
    is_equal = (product - a * multiplier) == 0
    return product, is_equal
if __name__ == '__main__':
    sample_a = 10
    sample_b = 25
    result_compare = compare_values(sample_a, sample_b)
    mult_result, equal_check = custom_calculation(5, 4)
    print(f"Comparison Result: {result_compare}")
    print(f"Custom Calculation Result: {mult_result}, Equality Check: {equal_check}")