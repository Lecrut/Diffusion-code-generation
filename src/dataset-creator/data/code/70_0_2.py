from typing import Tuple
def compare_distances(d1: float, d2: float) -> Tuple[float, float]:
    if d1 > d2:
        return d1, d1 - d2
    else:
        return d2, d2 - d1
if __name__ == '__main__':
    dist_a = 45.6789
    dist_b = 30.1234
    larger_dist, difference = compare_distances(dist_a, dist_b)
    print(f"Larger distance: {larger_dist}")
    print(f"Difference: {difference}")