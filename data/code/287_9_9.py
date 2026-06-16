import math
def find_most_weight_efficient_storage(measurements):
    if not measurements:
        return None, 0, 0
    n = len(measurements)
    min_total_weight = float('inf')
    best_grouping = []
    for i in range(1 << n):
        current_group = []
        current_weight = 0
        for j in range(n):
            if (i >> j) & 1:
                current_group.append(measurements[j])
                current_weight += measurements[j]
        if not current_group:
            continue
        data_size = sum(current_group)
        if data_size < min_total_weight:
            min_total_weight = data_size
            best_grouping = current_group
    if not best_grouping:
        return None, 0, 0
    return best_grouping, min_total_weight, n
if __name__ == '__main__':
    sample_measurements = [10, 5, 20, 3, 15]
    best_set, min_size, num_elements = find_most_weight_efficient_storage(sample_measurements)
    print(f"Original Measurements: {sample_measurements}")
    print(f"Most Weight-Efficient Grouping (Minimal Sum): {best_set}")
    print(f"Minimum Total Data Size Found: {min_size}")
    print(f"Number of Elements in Optimal Group: {num_elements}")