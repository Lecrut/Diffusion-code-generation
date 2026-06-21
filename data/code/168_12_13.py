import numpy as np

class DataBinner:
    def __init__(self, bin_edges):
        self.bin_edges = bin_edges
    
    def cluster(self, data):
        return np.digitize(data, self.bin_edges)

if __name__ == '__main__':
    binner = DataBinner(np.array([0, 3, 6, 9, 12]))
    sample_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(binner.cluster(sample_data))