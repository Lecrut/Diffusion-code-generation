import numpy as np

def validate_input(data, bin_edges):
    if not isinstance(data, np.ndarray) or not isinstance(bin_edges, np.ndarray):
        raise ValueError("Both data and bin_edges must be numpy arrays")
    if len(bin_edges) < 2:
        raise ValueError("bin_edges must contain at least two elements")

def cluster_into_bins(data, bin_edges):
    validate_input(data, bin_edges)
    return np.digitize(data, bin_edges)

if __name__ == '__main__':
    sample_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    bin_edges = np.array([0, 3, 6, 9, 12])
    print(cluster_into_bins(sample_data, bin_edges))