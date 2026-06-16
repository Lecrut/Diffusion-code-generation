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
    product = x * y
    is_even_condition = (product - 1) % 2 == 0
    return product, is_even_condition
if __name__ == '__main__':
    val_a, val_b = 5, 3
    result_compare = compare_values(val_a, val_b)
    prod_result, even_check = custom_operation(val_a, val_b)
    print(f"Comparison Result: {result_compare}")
    print(f"Custom Operation Product: {prod_result}, Even Check: {even_check}")