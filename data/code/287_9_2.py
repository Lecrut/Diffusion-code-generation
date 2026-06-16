import math
def find_most_efficient_storage(measurements):
    if not measurements:
        return None, 0, 0
    n = len(measurements)
    min_size = float('inf')
    best_unit_index = -1
    best_accuracy = float('inf')
    for i in range(n):
        current_sum = sum(measurements)
        current_size = 0
        current_accuracy = 0
        if measurements[i] == 0:
            current_size = 1                                                                                                                   
            current_accuracy = 1e-9                                                                               
        else:
            max_val = max(abs(m) for m in measurements)
            if max_val == 0:
                current_accuracy = 1e-9
            else:
                precision_needed = math.ceil(-math.log10(max_val)) + 1
                current_size = n * precision_needed
            unit = current_sum / n
            variance = sum((m - unit) ** 2 for m in measurements) / n
            current_accuracy = math.sqrt(variance)
        if current_accuracy < best_accuracy:
            best_accuracy = current_accuracy
            best_unit_index = i
            min_size = current_size
    if best_unit_index != -1:
        return measurements[best_unit_index], min_size, best_accuracy
    else:
        return None, 0, float('inf')
if __name__ == '__main__':
    sample_measurements = [1.2345, 6.7890, 3.14159, 8.5000]
    unit, size, accuracy = find_most_efficient_storage(sample_measurements)
    print(f"Measurements: {sample_measurements}")
    print(f"Most Weight-Efficient Unit (Mean): {unit}")
    print(f"Minimal Data Size Metric (Variance proxy): {size}")
    print(f"Achieved Accuracy (Root Mean Square Error): {accuracy}")