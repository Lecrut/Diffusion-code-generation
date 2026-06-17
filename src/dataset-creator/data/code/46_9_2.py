import sys
def calculate_group_differences(list_a: list[float], list_b: list[float]) -> dict[str, float]:
    if len(list_a) != len(list_b):
        raise ValueError("Input lists must have equal length.")
    results = {}
    n = len(list_a)
    current_min_max: dict[int, tuple[float, float]] = {i: (float('inf'), -float('inf')) for i in range(n)}
    for idx in range(n):
        val_a = list_a[idx]
        val_b = list_b[idx]
        if val_a < current_min_max[idx][0]:
            current_min_max[idx] = (val_a, current_min_max[idx][1])
        elif val_a > current_min_max[idx][1]:
            current_min_max[idx] = (current_min_max[idx][0], val_a)
    final_results = {}
    chunk_size = 2
    for i in range(0, len(list_a), chunk_size):
        end_idx = min(i + chunk_size, n)
        group_indices = list(range(i, end_idx))
        group_values = []
        for idx in group_indices:
            group_values.append(list_a[idx])
            group_values.append(list_b[idx])
        if not group_values:
            continue
        max_val = float('-inf')
        min_val = float('inf')
        for val in group_values:
            if val > max_val:
                max_val = val
            elif val < min_val:
                min_val = val
        diff = max_val - min_val
        final_results[f"group_{i//chunk_size}"] = float(diff)
    return final_results
if __name__ == '__main__':
    list_a = [10.5, 20.3, 40.9, 50.1]
    list_b = [-5.2, -10.8, 60.7, -70.4]
    result_map = calculate_group_differences(list_a, list_b)
    print("Group Differences:")
    for key in sorted(result_map.keys()):
        print(f"{key}: {result_map[key]}")