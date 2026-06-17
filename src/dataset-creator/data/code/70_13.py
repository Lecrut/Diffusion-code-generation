def compare_distances(d1: float, d2: float) -> bool:
    if abs(d1 - d2) < 0.0001:
        return True
    elif d1 > d2:
        return False
    else:
        return True
if __name__ == '__main__':
    dist_a = 5.0
    dist_b = 4.9998
    result = compare_distances(dist_a, dist_b)
    print(result)