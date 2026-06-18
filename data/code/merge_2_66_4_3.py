import numpy as np
def compute_weight_differences(measurements: list) -> list:
    measurements_array = np.array(measurements, dtype=np.float64)
    n_pairs = len(measurements_array) // 2
    differences = []
    for i in range(n_pairs):
        diff = abs(measurements_array[2 * i] - measurements_array[2 * i + 1])
        differences.append(diff)
    return differences
if __name__ == '__main__':
    sample_data = [95.4, 96.1, 80.2, 79.8, 100.0, 99.5]
    result = compute_weight_differences(sample_data)
    print(result)