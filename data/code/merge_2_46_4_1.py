import numpy as np
def compute_pairwise_differences(values: list[float]) -> np.ndarray:
    arr = np.array(values)
    diff_matrix = np.subtract.outer(arr, arr)
    return diff_matrix
if __name__ == '__main__':
    sample_values = [1.5, 2.3, -0.7, 4.1]
    result = compute_pairwise_differences(sample_values)
    print(result)