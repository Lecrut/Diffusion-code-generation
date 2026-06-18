def compare_distances(d1: float, d2: float) -> tuple[float, float]:
    larger = max(d1, d2)
    smaller = min(d1, d2)
    difference = abs(larger - smaller)
    return larger, difference
if __name__ == '__main__':
    dist_a = 5.7
    dist_b = 3.2
    result_larger, result_diff = compare_distances(dist_a, dist_b)
    print(f"Larger distance: {result_larger}")
    print(f"Difference: {result_diff}")