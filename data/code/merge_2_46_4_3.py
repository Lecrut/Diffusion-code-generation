import numpy as np
def compute_pairwise_differences(values: list[float]) -> tuple[list[int], list[float]]:
    arr = np.array(values)
    diff_matrix = np.subtract.outer(arr, arr)
    indices = []
    diffs = []
    for i in range(len(diff_matrix)):
        row_indices = [i] * len(diff_matrix[i])
        col_indices = list(range(len(diff_matrix)))
        indices.extend(row_indices + col_indices)
        diffs.extend(list(diff_matrix[i]))
    return indices, diffs
if __name__ == '__main__':
    sample_values = [1.5, 2.7, 3.9]
    idx_list, diff_list = compute_pairwise_differences(sample_values)
    print(f"Indices: {idx_list}")
    print(f"Diffs: {diff_list}")