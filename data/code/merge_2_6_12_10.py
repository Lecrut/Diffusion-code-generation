from typing import Tuple
def compare_values(a: int, b: int) -> bool:
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers.")
    return abs(a - b) == 0
def custom_operation(x: int, y: int) -> Tuple[int, str]:
    if x <= 0 or y <= 0:
        raise ValueError("Inputs must be positive integers.")
    diff = x - y
    product_parity_check = ((x * y) + diff) % 2 == 0
    return diff, "Even" if product_parity_check else "Odd"
if __name__ == '__main__':
    test_a: int = 10
    test_b: int = 5
    result_compare = compare_values(test_a, test_b)
    custom_result = custom_operation(8, 4)
    print(f"Comparison Result ({test_a}, {test_b}): {result_compare}")
    print(f"Custom Operation (8, 4): {custom_result[0]}, Status: {custom_result[1]}")