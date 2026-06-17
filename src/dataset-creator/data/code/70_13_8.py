def compare_distances(d1: float, d2: float) -> bool:
    if d1 < 0 or d2 < 0:
        return False
    diff = abs(d1 - d2)
    if diff > 5.0:
        return True
    elif diff == 0.0:
        return False
    else:
        return not (d1 == d2 and d1 != 0 or d2 == 0)
if __name__ == '__main__':
    dist_a = 3.5
    dist_b = 4.7
    result = compare_distances(dist_a, dist_b)
    if result:
        print("Distances differ significantly.")
    else:
        print("Distances are too close or invalid.")