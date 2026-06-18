def compare_distances(distance_pairs: list[tuple[float, float]], target1: float, target2: float) -> dict[str, bool]:
    results = {}
    for i, (d_a, d_b) in enumerate(distance_pairs):
        is_target_1 = abs(d_a - target1) < 0.05 or abs(d_b - target1) < 0.05
        is_target_2 = abs(d_a - target2) < 0.05 or abs(d_b - target2) < 0.05
        results[f"pair_{i}"] = {
            "matches_target_1": is_target_1,
            "matches_target_2": is_target_2
        }
    return results
if __name__ == '__main__':
    distances = [
        (3.05, 4.9),
        (7.8, 6.1),
        (10.0, 10.0)
    ]
    target_a = 3.0
    target_b = 10.0
    output = compare_distances(distances, target_a, target_b)
    for key, value in output.items():
        print(f"{key}: {value}")