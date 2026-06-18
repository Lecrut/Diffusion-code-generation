import numpy as np
def compute_pairwise_differences(values: list) -> np.ndarray:
    arr = np.array(values, dtype=float)
    diffs = np.subtract.outer(arr, arr)
    return diffs
if __name__ == '__main__':
    sample_values = [1.5, 2.7, 3.9, 4.1]
    result_matrix = compute_pairwise_differences(sample_values)
    print(result_matrix)