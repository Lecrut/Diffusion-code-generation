def compare_distances(dist1: float, dist2: float) -> tuple[float, float]:
    larger = max(dist1, dist2)
    smaller = min(dist1, dist2)
    difference = abs(larger - smaller)
    return (larger, difference)
if __name__ == '__main__':
    val1 = 50.75
    val2 = 30.25
    result_larger, diff = compare_distances(val1, val2)
    print(f"Larger distance: {result_larger}")
    print(f"Difference: {diff}")