import math
def find_most_efficient_storage(measurements):
    if not measurements:
        return None, 0, 0
    n = len(measurements)
    total_weight = sum(abs(m) for m in measurements)
    best_storage_size = float('inf')
    best_storage_config = None
    current_storage_size = n * 8                                               
    best_storage_size = current_storage_size
    best_storage_config = {"method": "Individual Storage", "size": current_storage_size, "weight_efficiency": total_weight / current_storage_size}
    if n > 0:
        aggregate_value = sum(measurements) / n
        aggregate_storage_size = 8  
        error = sum(abs(m - aggregate_value) for m in measurements) / n
        aggregate_weight_efficiency = total_weight / aggregate_storage_size
        if aggregate_weight_efficiency > best_storage_config["weight_efficiency"]:
            best_storage_size = aggregate_storage_size
            best_storage_config = {"method": "Aggregate (Mean)", "size": aggregate_storage_size, "weight_efficiency": aggregate_weight_efficiency}
    return best_storage_config, total_weight, n
if __name__ == '__main__':
    sample_measurements = [1.0, 2.5, 3.0, 4.5, 5.0]
    result_config, total_w, count = find_most_efficient_storage(sample_measurements)
    print(f"Measurements: {sample_measurements}")
    print("-" * 40)
    print(f"Total Weight (Sum of absolute values): {total_w:.2f}")
    print(f"Number of Measurements: {count}")
    print("\nMost Weight-Efficient Storage Configuration:")
    print(f"Method: {result_config['method']}")
    print(f"Data Size (Units): {result_config['size']}")
    print(f"Weight Efficiency (Total Weight / Data Size): {result_config['weight_efficiency']:.4f}")