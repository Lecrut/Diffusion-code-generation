import numpy as np

def validate_data(data):
    if not isinstance(data, np.ndarray) or data.ndim != 1:
        raise ValueError("Data must be a 1-dimensional numpy array.")
    if not data.size > 0:
        raise ValueError("Data array cannot be empty.")

def validate_bin_edges(bin_edges):
    if not isinstance(bin_edges, np.ndarray) or bin_edges.ndim != 1:
        raise ValueError("Bin edges must be a 1-dimensional numpy array.")
    if not all(bin_edges[i] < bin_edges[i + 1] for i in range(len(bin_edges) - 1)):
        raise ValueError("Bin edges must be monotonically increasing.")

def cluster_into_bins(data, bin_edges):
    validate_data(data)
    validate_bin_edges(bin_edges)
    return np.digitize(data, bin_edges)

if __name__ == '__main__':
    sample_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    bin_edges = np.array([0, 3, 6, 9, 12])
    result = cluster_into_bins(sample_data, bin_edges)
    print(result)