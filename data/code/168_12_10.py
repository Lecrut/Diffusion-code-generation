import numpy as np

def cluster_data(data, bins):
    return np.digitize(data, bins)

if __name__ == '__main__':
    data = np.array([10, 20, 30, 40, 50])
    bins = np.array([0, 25, 50])
    print(cluster_data(data, bins))