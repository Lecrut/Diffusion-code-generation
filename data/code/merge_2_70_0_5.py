def compare_distances(val_a: float, val_b: float) -> tuple[float, float]:
    if not isinstance(val_a, (int, float)) or not isinstance(val_b, (int, float)):
        raise TypeError("Both values must be numeric.")
    larger_value = max(val_a, val_b)
    difference = abs(larger_value - min(val_a, val_b))
    return larger_value, difference
if __name__ == '__main__':
    distance_x: float = 150.75
    distance_y: float = 234.9
    result_larger, result_diff = compare_distances(distance_x, distance_y)
    print(f"Larger value: {result_larger}")
    print(f"Difference: {result_diff}")