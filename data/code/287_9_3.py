import math
def find_most_efficient_storage(measurements):
    if not measurements:
        return None, 0.0
    n = len(measurements)
    min_size = float('inf')
    best_unit = None
    best_accuracy = float('inf')
    for i in range(1, n + 1):
        current_sum = sum(measurements[:i])
        current_mean = current_sum / i
        current_variance = sum([(x - current_mean) ** 2 for x in measurements[:i]]) / i
        current_size = i                       
        if current_size < min_size:
            min_size = current_size
            best_unit = i
            best_accuracy = current_variance
        elif current_size == min_size:
            if current_variance < best_accuracy:
                best_unit = i
                best_accuracy = current_variance
    return best_unit, best_accuracy
if __name__ == '__main__':
    sample_measurements = [10.0, 12.0, 15.0, 11.0, 13.0, 14.0]
    best_k, accuracy = find_most_efficient_storage(sample_measurements)
    print(f"Sample Measurements: {sample_measurements}")
    print(f"Most Weight-Efficient Unit Size (k): {best_k}")
    print(f"Resulting Variance (Accuracy Metric): {accuracy}")