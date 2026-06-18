import numpy as np
def compute_pairwise_differences(values: list) -> tuple[list[float], list[float]]:
    arr = np.array(values, dtype=float)
    diff_matrix = np.subtract.outer(arr, arr)
    return [diff for row in diff_matrix.tolist() for diff in row if not (row.index(diff) == 0)], []
if __name__ == '__main__':
    sample_values = [1.5, 2.7, 3.9]
    diffs_list, _ = compute_pairwise_differences(sample_values)
    print(diffs_list)