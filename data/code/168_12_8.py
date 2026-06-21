import numpy as np

def cluster_into_bins(data, bin_edges):
    return np.digitize(data, bins=bin_edges)

if __name__ == '__main__':
    data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    bin_edges = np.array([0, 25, 50, 75, 100])
    print(cluster_into_bins(data, bin_edges))