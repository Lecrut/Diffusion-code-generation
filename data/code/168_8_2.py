import numpy as np
def bin_data(data, bins):
    if not data:
        return [], []
    lower_bounds = np.array(bins[:-1])
    upper_bounds = np.array(bins[1:])
    labels = []
    binned_data = []
    for x in data:
        bin_index = np.searchsorted(lower_bounds, x)
        if bin_index == len(lower_bounds):
            if x <= upper_bounds[-1]:
                bin_index = len(lower_bounds) - 1
            else:
                bin_index = len(lower_bounds) - 1
        label = f"{lower_bounds[bin_index]} to {upper_bounds[bin_index]}"
        labels.append(label)
        binned_data.append(x)
    return labels, binned_data
if __name__ == '__main__':
    data_points = [1.2, 5.5, 10.1, 15.0, 22.3, 30.0, 35.5, 40.0]
    bin_edges = [0, 10, 20, 30, 40, 50]
    labels, binned = bin_data(data_points, bin_edges)
    print("Data Points:", data_points)
    print("Bin Edges:", bin_edges)
    print("Labels:", labels)
    print("Binned Data:", binned)