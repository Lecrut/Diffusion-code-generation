import numpy as np

def cluster_into_bins(data, bin_edges):
    return np.digitize(data, bin_edges)

if __name__ == '__main__':
    sample_data = np.array([10, 20, 30, 40, 50])
    bin_edges = np.array([0, 25, 50])
    print(cluster_into_bins(sample_data, bin_edges))