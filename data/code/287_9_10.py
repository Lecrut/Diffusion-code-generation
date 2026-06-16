import math
def find_most_efficient_storage(measurements):
    if not measurements:
        return None, 0, 0
    n = len(measurements)
    total_weight = sum(abs(m) for m in measurements)
    best_storage_size = float('inf')
    best_storage_config = None
    baseline_size = n * 8                                                      
    best_storage_size = baseline_size
    best_storage_config = {"type": "individual", "size": baseline_size, "accuracy_loss": 0}
    if n > 0:
        mean_value = sum(measurements) / n
        storage_size_mean = 8                                   
        accuracy_loss_mean = total_weight * (1 - abs(mean_value) / total_weight) if total_weight > 0 else 0
        if storage_size_mean < best_storage_size:
            best_storage_size = storage_size_mean
            best_storage_config = {"type": "mean", "size": storage_size_mean, "accuracy_loss": accuracy_loss_mean}
    min_val = min(measurements)
    max_val = max(measurements)
    range_size = abs(max_val - min_val)
    storage_size_range = 8                                
    accuracy_loss_range = (1 - range_size / total_weight) if total_weight > 0 else 0
    if storage_size_range < best_storage_size:
        best_storage_size = storage_size_range
        best_storage_config = {"type": "range", "size": storage_size_range, "accuracy_loss": accuracy_loss_range}
    return best_storage_config, total_weight, best_storage_size
if __name__ == '__main__':
    sample_measurements = [1.0, 2.5, 3.0, 4.5, 5.0]
    result_config, total_w, final_size = find_most_efficient_storage(sample_measurements)
    print(f"Sample Measurements: {sample_measurements}")
    print("-" * 30)
    print(f"Total Weight (Sum of Abs Values): {total_w:.2f}")
    print(f"Most Weight-Efficient Storage Configuration:")
    print(f"  Type: {result_config['type']}")
    print(f"  Data Size (Bits/Units): {result_config['size']}")
    print(f"  Estimated Accuracy Loss Factor: {result_config['accuracy_loss']:.4f}")