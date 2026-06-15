import numpy as np
def analyze_and_optimize(data):
    if not isinstance(data, np.ndarray):
        data = np.array(data)
    mean_val = np.mean(data)
    std_dev = np.std(data)
    variance = np.var(data)
    sum_sq_diff = np.sum((data - mean_val)**2)
    return {
        "mean": mean_val,
        "std_dev": std_dev,
        "variance": variance,
        "sum_sq_diff": sum_sq_diff
    }
if __name__ == '__main__':
    sample_data = [1.5, 2.5, 3.5, 4.5, 5.5]
    results = analyze_and_optimize(sample_data)
    print(results)