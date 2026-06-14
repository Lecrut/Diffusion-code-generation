import numpy as np
def analyze_and_optimize(data):
    if not isinstance(data, np.ndarray):
        data = np.array(data)
    mean_val = np.mean(data)
    std_dev = np.std(data)
    variance = np.var(data)
    return mean_val, std_dev, variance
if __name__ == '__main__':
    sample_data = [10, 12, 23, 23, 16, 23, 21, 16]
    results = analyze_and_optimize(sample_data)
    mean, std, var = results
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {std}")
    print(f"Variance: {var}")