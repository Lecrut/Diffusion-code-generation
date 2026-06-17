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
    data_pairs = [(10.5, 20.3), (9.8, 21.1), (10.6, 19.9)]
    t1, t2 = 10.5, 20.0
    output = compare_distances(data_pairs, t1, t2)
    for key, val in output.items():
        print(f"{key}: Target1={val['matches_target_1']}, Target2={val['matches_target_2']}")