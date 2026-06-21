import numpy as np

def cluster_into_bins(data, bin_edges):
    return np.digitize(data, bin_edges)

if __name__ == '__main__':
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    bin_edges = np.array([2, 4, 6, 8, 10])
    print(cluster_into_bins(data, bin_edges))