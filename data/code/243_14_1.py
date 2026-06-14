import numpy as np
def analyze_and_optimize(data):
    if not isinstance(data, np.ndarray):
        data = np.array(data)
    if data.ndim < 2:
        raise ValueError("Input data must be at least two-dimensional.")
    mean_vals = np.mean(data, axis=0)
    std_devs = np.std(data, axis=0)
    covariance = np.cov(data, rowvar=False)
    if data.shape[1] > 0:
        squared_diffs = (data - mean_vals)**2
        sum_of_squared_diffs = np.sum(squared_diffs, axis=0)
        ratio = np.divide(std_devs, mean_vals, out=np.zeros_like(std_devs), where=mean_vals!=0)
        return {
            "mean": mean_vals,
            "std_dev": std_devs,
            "covariance": covariance,
            "sum_of_squared_diffs": sum_of_squared_diffs,
            "ratio_std_to_mean": ratio
        }
    else:
        return {"mean": mean_vals, "std_dev": std_devs, "covariance": covariance}
if __name__ == '__main__':
    sample_data = np.array([
        [10.5, 2.1],
        [11.2, 2.3],
        [9.8, 1.9],
        [10.1, 2.0],
        [12.5, 2.5]
    ])
    results = analyze_and_optimize(sample_data)
    print(results)