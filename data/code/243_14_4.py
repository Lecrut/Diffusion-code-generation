import numpy as np
def analyze_and_optimize(data):
    if not isinstance(data, np.ndarray):
        data = np.array(data)
    if data.ndim != 2:
        raise ValueError("Input must be a 2D array.")
    means = np.mean(data, axis=1)
    stds = np.std(data, axis=1)
    overall_variance = np.var(data)
    return means, stds, overall_variance
if __name__ == '__main__':
    sample_data = np.array([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0],
        [10.0, 11.0, 12.0]
    ])
    means, stds, overall_variance = analyze_and_optimize(sample_data)
    print(f"Means per row: {means}")
    print(f"Standard Deviations per row: {stds}")
    print(f"Overall Variance of the dataset: {overall_variance}")