import numpy as np
def compute_weight_differences(measurements: list) -> float:
    measurements_array = np.array(measurements, dtype=np.float64)
    differences = np.diff(measurements_array).astype(np.int32)
    return sum(differences) / len(differences - 1) if len(differences) > 0 else 0.0
if __name__ == '__main__':
    sample_data = [50, 48, 52, 49]
    result = compute_weight_differences(sample_data)
    print(result)