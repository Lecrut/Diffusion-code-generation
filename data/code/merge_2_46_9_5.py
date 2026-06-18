import sys
def robust_range(values):
    if not values:
        return 0.0
    max_val = float('-inf')
    min_val = float('inf')
    for v in values:
        try:
            num_v = float(v)
        except (ValueError, TypeError):
            continue
        if num_v > max_val:
            max_val = num_v
        elif num_v < min_val:
            min_val = num_v
    return max(0.0, max_val - min_val)
def group_parallel_lists(list_a, list_b):
    result_groups = []
    if len(list_a) != len(list_b):
        raise ValueError("Lists must be of equal length")
    for i in range(len(list_a)):
        pair_values = [list_a[i], list_b[i]]
        group_range = robust_range(pair_values)
        result_groups.append({
            'index': i,
            'values': pair_values,
            'range': group_range
        })
    return result_groups
if __name__ == '__main__':
    sample_list_a = [10.5, 23.4, -5.6, 999.9]
    sample_list_b = [-1.2, 87.1, 0.0, 1000.0]
    result = group_parallel_lists(sample_list_a, sample_list_b)
    for item in result:
        print(f"Group {item['index']}: Values={item['values']}, Range={item['range']}")