from typing import Tuple
def compare_values(a: int, b: int) -> bool:
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers.")
    return a == b
def custom_calc(a: int, b: int) -> Tuple[int, int]:
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers.")
    diff = a - b
    prod = a * b
    return diff, prod
if __name__ == '__main__':
    sample_a = 15
    sample_b = 7
    result_comparison = compare_values(sample_a, sample_b)
    res_sub, res_mul = custom_calc(sample_a, sample_b)
    print(f"Comparison Result: {result_comparison}")
    print(f"Custom Calculation - Subtraction: {res_sub}, Multiplication: {res_mul}")