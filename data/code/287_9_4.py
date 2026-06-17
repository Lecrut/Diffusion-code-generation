import math
def find_most_efficient_storage(measurements):
    if not measurements:
        return None, 0, 0
    n = len(measurements)
    min_size = float('inf')
    best_unit = None
    best_accuracy = float('inf')
    for i in range(1, n + 1):
        current_sum = sum(measurements[:i])
        current_mean = current_sum / i
        current_variance = sum((x - current_mean) ** 2 for x in measurements[:i]) / i
        current_size = i                                                                  
        if current_size < min_size:
            min_size = current_size
            best_unit = i
            best_accuracy = math.sqrt(sum((x - current_mean) ** 2 for x in measurements[:i]) / i)
        elif current_size == min_size:
            current_accuracy = math.sqrt(sum((x - current_mean) ** 2 for x in measurements[:i]) / i)
            if current_accuracy < best_accuracy:
                best_unit = i
                best_accuracy = current_accuracy
    return best_unit, min_size, best_accuracy
if __name__ == '__main__':
    sample_measurements = [10, 12, 15, 11, 13, 14, 16]
    best_k, size, accuracy = find_most_efficient_storage(sample_measurements)
    print(f"Sample Measurements: {sample_measurements}")
    print(f"Most Weight-Efficient Unit (Number of measurements): {best_k}")
    print(f"Minimal Data Size (Count): {size}")
    print(f"Achieved Accuracy (Standard Deviation): {accuracy:.4f}")