import numpy as np
def compute_weight_differences(measurements: list) -> float:
    if len(measurements) % 2 != 0:
        raise ValueError("Number of measurements must be even.")
    n = len(measurements) // 2
    arr = np.array(measurements, dtype=np.float64)
    diffs = np.abs(arr[:n] - arr[n:])
    return float(np.sum(diffs))
if __name__ == '__main__':
    sample_data = [10.5, 9.8, 20.3, 19.7, 30.1, 29.6, 40.0, 39.5]
    result = compute_weight_differences(sample_data)
    print(result)