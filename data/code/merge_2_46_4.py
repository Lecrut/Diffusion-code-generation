import numpy as np
def compute_pairwise_differences(values: list[float]) -> tuple[list[float], float]:
    arr = np.array(values)
    n = len(arr)
    diff_matrix = np.abs(np.subtract.outer(arr, arr))
    mask = ~np.eye(n, dtype=bool)
    differences = diff_matrix[mask]
    return list(differences), sum(differences)
if __name__ == '__main__':
    sample_values = [1.5, 2.3, 4.7, -0.9, 6.1]
    diffs, total_diff = compute_pairwise_differences(sample_values)
    print(f"Input values: {sample_values}")
    print(f"Pairwise absolute differences (excluding self): {diffs}")
    print(f"Sum of all pairwise differences: {total_diff:.4f}")