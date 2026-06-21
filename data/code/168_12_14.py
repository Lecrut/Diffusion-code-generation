import numpy as np

def validate_data_and_bin_edges(data, bin_edges):
    if not isinstance(data, np.ndarray) or data.ndim != 1:
        raise ValueError("Data must be a 1D numpy array.")
    if not isinstance(bin_edges, np.ndarray) or bin_edges.ndim != 1 or len(bin_edges) < 2:
        raise ValueError("Bin edges must be a 1D numpy array with at least two elements.")

def cluster_into_bins(data, bin_edges):
    validate_data_and_bin_edges(data, bin_edges)
    return np.digitize(data, bin_edges)

if __name__ == '__main__':
    sample_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    bin_edges = np.array([0, 3, 6, 9, 12])
    print(cluster_into_bins(sample_data, bin_edges))