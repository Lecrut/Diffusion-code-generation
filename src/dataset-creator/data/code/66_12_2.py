import numpy as np
def calculate_weight_differences(weights1: list[float], weights2: list[float]) -> float:
    arr1 = np.array(weights1)
    arr2 = np.array(weights2)
    if len(arr1) != len(arr2):
        raise ValueError("Arrays must have the same length")
    diff_array = arr1 - arr2
    return float(np.sum(diff_array))
if __name__ == '__main__':
    sample_weights_1 = [70.5, 68.3, 72.1, 69.8]
    sample_weights_2 = [71.0, 68.5, 71.9, 70.2]
    result = calculate_weight_differences(sample_weights_1, sample_weights_2)
    print(result)