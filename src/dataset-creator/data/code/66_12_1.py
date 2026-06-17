import numpy as np
def calculate_weight_diffs(weights1: list[float], weights2: list[float]) -> np.ndarray:
    arr1 = np.array(weights1)
    arr2 = np.array(weights2)
    return arr1 - arr2
if __name__ == '__main__':
    sample_weights_1 = [70.5, 68.3, 72.1, 69.8]
    sample_weights_2 = [71.0, 67.5, 73.2, 68.4]
    result = calculate_weight_diffs(sample_weights_1, sample_weights_2)
    print(result)