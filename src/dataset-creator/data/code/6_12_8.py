from typing import Tuple
def compare_values(a: int, b: int) -> bool:
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers.")
    return a == b
def custom_operation(a: int, b: int) -> Tuple[int, bool]:
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers.")
    difference = a - b
    product_check = (a * b == 100)
    return difference, product_check
if __name__ == '__main__':
    sample_a = 5
    sample_b = 5
    result_compare = compare_values(sample_a, sample_b)
    diff_result, prod_result = custom_operation(sample_a, sample_b)
    print(f"Comparison Result: {result_compare}")
    print(f"Difference and Product Check: ({diff_result}, {prod_result})")