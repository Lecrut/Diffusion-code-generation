def compare_distances(d1: float, d2: float) -> tuple[float, float]:
    if d1 >= d2:
        larger = d1
        difference = d1 - d2
    else:
        larger = d2
        difference = d2 - d1
    return larger, difference
if __name__ == '__main__':
    dist_a = 5.7
    dist_b = 3.2
    result_larger, result_diff = compare_distances(dist_a, dist_b)
    print(f"Larger distance: {result_larger}")
    print(f"Difference: {result_diff}")