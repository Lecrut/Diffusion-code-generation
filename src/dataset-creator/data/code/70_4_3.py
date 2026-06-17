def compare_distances(distance_pairs: tuple[tuple[float, float], ...], target1: float, target2: float) -> list[bool]:
    return [pair[0] == pair[1] for pair in distance_pairs if abs(pair[0] - target1) < 0.001 and abs(pair[1] - target2) < 0.001 or abs(pair[0] - target2) < 0.001 and abs(pair[1] - target1) < 0.001]
if __name__ == '__main__':
    distances = ((3, 4), (5, 12), (6, 8))
    targets_a = (3, 4)
    targets_b = (5, 12)
    results = compare_distances(distances, *targets_a) + compare_distances(distances, *targets_b)
    print(results)