def compare_distances(distance_pairs: list[tuple[float, float]], target1: float, target2: float) -> dict[str, bool]:
    results = {}
    for i in range(len(distance_pairs)):
        d_pair = distance_pairs[i]
        if abs(d_pair[0] - target1) < 0.05 and abs(d_pair[1] - target2) < 0.05:
            results[f"pair_{i}"] = True
        else:
            results[f"pair_{i}"] = False
    return results
if __name__ == '__main__':
    distances = [(3.14, 6.28), (1.57, 9.42), (0.0, 0.0)]
    t1, t2 = 3.14, 6.28
    matches = compare_distances(distances, t1, t2)
    for key, value in matches.items():
        print(f"{key}: {value}")