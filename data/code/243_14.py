import numpy as np
def analyze_and_optimize(data):
    if not isinstance(data, np.ndarray):
        data = np.array(data)
    if data.ndim < 2:
        return None
    mean_val = np.mean(data, axis=0)
    std_dev = np.std(data, axis=0)
    covariance = np.cov(data, rowvar=False)
    return mean_val, std_dev, covariance
if __name__ == '__main__':
    sample_data = np.array([
        [1.0, 2.5, 3.0],
        [2.0, 4.5, 5.5],
        [3.0, 6.0, 7.5],
        [4.0, 8.0, 9.5]
    ])
    mean, std, cov = analyze_and_optimize(sample_data)
    print("Mean:\n", mean)
    print("\nStandard Deviation:\n", std)
    print("\nCovariance:\n", cov)