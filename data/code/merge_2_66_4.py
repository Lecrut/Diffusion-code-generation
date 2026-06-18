import numpy as np
def compute_weight_differences(measurements: list) -> list:
    measurements_array = np.array(measurements, dtype=np.float64)
    differences = []
    for i in range(0, len(measurements), 2):
        if i + 1 < len(measurements):
            diff = abs(measurements_array[i] - measurements_array[i+1])
            differences.append(diff)
        else:
            break
    return differences
if __name__ == '__main__':
    sample_data = [95.2, 94.8, 102.3, 101.9, 88.7, 89.1]
    result = compute_weight_differences(sample_data)
    print(result)