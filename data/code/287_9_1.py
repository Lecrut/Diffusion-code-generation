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
        if measurements[i] != 0:
            current_size = abs(measurements[i])
            current_accuracy = 1.0                                                     
        else:
            current_size = 0
            current_accuracy = 0.0
        if current_size < min_size:
            min_size = current_size
            best_unit_index = i
            best_accuracy = current_accuracy
        elif current_size == min_size:
            if current_accuracy > best_accuracy:
                best_unit_index = i
                best_accuracy = current_accuracy
    if best_unit_index != -1:
        return measurements[best_unit_index], min_size, best_accuracy
    else:
        return None, 0, 0
if __name__ == '__main__':
    sample_measurements = [10.5, -5.2, 3.14, 0, 8.8, -1.0]
    result_value, result_size, result_accuracy = find_most_efficient_storage(sample_measurements)
    print(f"Original Measurements: {sample_measurements}")
    print(f"Most Weight-Efficient Unit Value: {result_value}")
    print(f"Minimal Data Size (Weight): {result_size}")
    print(f"Accuracy Metric: {result_accuracy}")