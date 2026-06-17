import numpy as np
def find_matching_elements(arr: np.ndarray, condition_value: float) -> list:
    arr = np.asarray(arr, dtype=float)
    tolerance = 1e-9
    mask = (np.abs(arr - condition_value)) < tolerance
    return [float(x) for x in arr[mask]]
if __name__ == '__main__':
    sample_array = [-3.5, 2.0, 4.7896, 1e-10, 0.0]
    target_value = -3.5
    results = find_matching_elements(sample_array, target_value)
    print(results)