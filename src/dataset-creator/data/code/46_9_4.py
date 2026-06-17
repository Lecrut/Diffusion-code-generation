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
        min_val, max_val = current_min_max[idx]
        if val_b < min_val:
            current_min_max[idx] = (val_b, max(max_val, val_a))
        elif val_b > max_val:
            current_min_max[idx] = (min(min_val, val_a), val_b)
    final_results = {}
    for idx in range(n):
        min_v, max_v = current_min_max[idx]
        diff = abs(max_v - min_v)                                                        
        group_key = f"group_{idx}"
        final_results[group_key] = float(diff)
    return final_results
if __name__ == '__main__':
    sample_list_a = [10.5, 23.4, -98765.43, 0.000001, 999999.9]
    sample_list_b = [5.2, 12.1, -1e-10, 42.0, 1e+10]
    result_map = calculate_group_differences(sample_list_a, sample_list_b)
    print("Group Differences:")
    for group_key in sorted(result_map.keys()):
        diff_value = result_map[group_key]
        formatted_diff = f"{diff_value:.6f}" if abs(diff_value - int(diff_value)) < 1e-5 else str(diff_value)
        print(f"  {group_key}: {formatted_diff}")