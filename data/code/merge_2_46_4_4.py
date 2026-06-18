import numpy as np
def compute_pairwise_differences(values: list[float]) -> tuple[list[float], list[float]]:
    arr = np.array(values)
    diff_matrix = np.subtract.outer(arr, arr)
    return [diff for row in diff_matrix for diff in row]
if __name__ == '__main__':
    sample_values = [1.5, 2.7, 3.9, 4.2]
    result = compute_pairwise_differences(sample_values)
    print(result)