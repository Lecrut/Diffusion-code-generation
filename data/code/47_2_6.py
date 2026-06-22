import numpy as np

def compute_mean(dataset):
    if not isinstance(dataset, (list, tuple, np.ndarray)):
        raise TypeError("Input must be a list, tuple, or numpy array")
    if len(dataset) == 0:
        raise ValueError("Input dataset must not be empty")
    for item in dataset:
        if not isinstance(item, (int, float, np.integer, np.floating)):
            raise TypeError("All elements in dataset must be numeric")
    return float(np.mean(dataset))

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = compute_mean(sample_data)
    print(result)