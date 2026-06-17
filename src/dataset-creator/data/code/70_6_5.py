def compare_distances(d1: float, d2: float) -> tuple[float, float]:
    if d1 >= d2:
        return (d1, d1 - d2)
    else:
        return (d2, d2 - d1)
if __name__ == '__main__':
    dist_a = 45.7
    dist_b = 30.2
    result_dist, diff = compare_distances(dist_a, dist_b)
    print(result_dist, diff)