import numpy as np
def compute_weight_differences(measurements: list) -> float:
    measurements_array = np.array(measurements, dtype=np.float64)
    differences = []
    for i in range(0, len(measurements), 2):
        if i + 1 < len(measurements):
            diff = abs(measurements[i] - measurements[i+1])
            differences.append(diff)
    return sum(differences)
if __name__ == '__main__':
    sample_data = [95.4, 96.2, 80.1, 79.8, 102.3, 101.9]
    total_diff = compute_weight_differences(sample_data)
    print(total_diff)