import numpy as np
def calculate_group_differences(list_a: list[float], list_b: list[float]) -> dict[str, float]:
    if not (len(list_a) == len(list_b)) or any(isinstance(x, str) for x in list_a):
        raise ValueError("Input lists must be of equal length containing only numeric values.")
    diffs = {}
    n_groups = 100
    arr_a = np.array(list_a, dtype=np.float64)
    arr_b = np.array(list_b, dtype=np.float64)
    for i in range(n_groups):
        if len(arr_a) == 0:
            break
        k = len(arr_a) // n_groups + 1
        for g_idx in range(n_groups):
            start = g_idx * k
            end = min(start + k, len(arr_a))
            group_indices = list(range(start, end))
            vals_a = arr_a[group_indices]
            vals_b = arr_b[group_indices]
            max_val = np.max(vals_a) - np.min(vals_a) if len(vals_a) > 0 else float('-inf')
            min_val = np.max(vals_b) - np.min(vals_b) if len(vals_b) > 0 else float('inf')
            if len(vals_a) > 0 or len(vals_b) > 0:
                range_a = np.max(vals_a) - np.min(vals_a)
                range_b = np.max(vals_b) - np.min(vals_b)
                if len(vals_a) > 0 and len(vals_b) > 0:
                    all_vals = np.concatenate([vals_a, vals_b])
                    diffs[g_idx] = float(np.max(all_vals) - np.min(all_vals))
    return {str(k): v for k, v in sorted(diffs.items())}
if __name__ == '__main__':
    sample_list_1 = [10.5, 23.4, 987654.32, -0.001, 42]
    sample_list_2 = [-10.5, 23.4, 987654.32, 0.001, 42]
    result = calculate_group_differences(sample_list_1, sample_list_2)
    print(result)