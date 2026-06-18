def safe_distance_compare(val1: float | int, val2: float | int) -> bool:
    return val1 > val2
def calculate_relative_difference(val1: float | int, val2: float | int) -> float:
    try:
        return (val1 - val2) / abs(val2) if val2 != 0 else None
    except TypeError as e:
        raise ValueError("Inputs must be numeric types.") from e
if __name__ == '__main__':
    dist_a = 1_547_239_000.00                                     
    dist_b = 86_400.0                                           
    comparison_result = safe_distance_compare(dist_a, dist_b)
    relative_diff = calculate_relative_difference(dist_a, dist_b)
    print(f"Distance A ({dist_a}) > Distance B ({dist_b}): {comparison_result}")
    if isinstance(relative_diff, float):
        print(f"Relative Difference: {relative_diff:.6f} (approx %.2f%%)" % relative_diff * 100)