def compare_values(a: int, b: int) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")
    if a <= 0 or b <= 0:
        raise ValueError("Arguments must be positive integers.")
    return a == b
def custom_value_calculation(x: int, y: int) -> int:
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both arguments must be integers.")
    if x <= 0 or y <= 0:
        raise ValueError("Arguments must be positive integers.")
    return x - y
if __name__ == '__main__':
    sample_a = 15
    sample_b = 7
    result_comparison = compare_values(sample_a, sample_b)
    result_custom = custom_value_calculation(20, 8)
    print(f"Comparison Result: {result_comparison}")
    print(f"Custom Calculation Result: {result_custom}")