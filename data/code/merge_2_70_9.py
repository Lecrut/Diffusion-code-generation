from typing import Tuple, Optional
def compare_distances(distance_a: float, distance_b: float) -> str:
    if not isinstance(distance_a, (int, float)) or not isinstance(distance_b, (int, float)):
        raise TypeError("Both arguments must be numeric.")
    if distance_a < 0 or distance_b < 0:
        raise ValueError("Distances cannot be negative.")
    if distance_a == distance_b:
        return "equal"
    diff = abs(distance_a - distance_b)
    max_val = max(abs(distance_a), abs(distance_b))
    if diff > 1e-9 * max(max_val, 1.0):
        return "greater" if distance_a > distance_b else "less"
    return "equal"
if __name__ == '__main__':
    val_1 = 1e308
    val_2 = 5 * (val_1 + 1)
    result_a = compare_distances(val_1, val_2)
    print(f"Comparison Result: {result_a}")
    int_large = 9007199254740993 * 2 + 1
    result_b = compare_distances(int_large, int_large)
    print(f"Integer Comparison Result: {result_b}")
    epsilon_val = 1e-10
    very_close_a = float(epsilon_val)
    very_close_b = float(2 * epsilon_val + 1e-15)
    result_c = compare_distances(very_close_a, very_close_b)
    print(f"Close Value Comparison Result: {result_c}")