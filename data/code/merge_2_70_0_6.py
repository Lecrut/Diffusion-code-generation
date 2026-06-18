def compare_distances(d1: float, d2: float) -> tuple[float, float]:
    larger = max(d1, d2)
    smaller = min(d1, d2)
    difference = abs(larger - smaller)
    return larger, difference
if __name__ == '__main__':
    val_a: float = 45.7
    val_b: float = 89.3
    result_larger, diff = compare_distances(val_a, val_b)
    print(f"Larger value: {result_larger}")
    print(f"Difference: {diff}")