import math
def find_most_efficient_storage(measurements):
    if not measurements:
        return None, 0, 0
    n = len(measurements)
    min_size = float('inf')
    best_group = []
    for i in range(1 << n):
        current_group_indices = []
        current_sum = 0
        current_count = 0
        for j in range(n):
            if (i >> j) & 1:
                current_group_indices.append(j)
                current_sum += measurements[j]
                current_count += 1
        if current_count > 0:
            data_size = current_count * 8                                                                            
            if data_size < min_size:
                min_size = data_size
                best_group = current_group_indices
    if not best_group:
        return None, 0, 0
    total_sum = sum(measurements[i] for i in best_group)
    return best_group, min_size, total_sum
if __name__ == '__main__':
    sample_measurements = [1.5, 2.7, 3.1, 4.9, 5.0, 6.2, 7.8]
    best_indices, min_size, total_sum = find_most_efficient_storage(sample_measurements)
    print(f"Original Measurements: {sample_measurements}")
    if best_indices:
        print(f"Most Weight-Efficient Group Indices: {best_indices}")
        print(f"Minimum Data Size (in bytes): {min_size}")
        print(f"Total Sum of Selected Measurements: {total_sum}")
    else:
        print("No efficient group found.")