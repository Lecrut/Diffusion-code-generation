import numpy as np
def bin_data(data, bins):
    if not data:
        return [], []
    lower_bounds = np.array(bins[:-1])
    upper_bounds = np.array(bins[1:])
    bins_labels = []
    binned_data = []
    for i in range(len(data)):
        value = data[i]
        bin_index = -1
        for j in range(len(lower_bounds)):
            if lower_bounds[j] <= value < upper_bounds[j]:
                bin_index = j
                break
        if bin_index != -1:
            bins_labels.append(f"{lower_bounds[bin_index]} to {upper_bounds[bin_index]}")
            binned_data.append(bin_index)
        else:
            bins_labels.append("Outside Range")
            binned_data.append(-1)
    return bins_labels, binned_data
if __name__ == '__main__':
    data_points = [1.2, 5.5, 10.1, 15.0, 22.3, 30.0, 35.5, 40.1]
    range_boundaries = [0, 10, 20, 30, 45]
    labels, indices = bin_data(data_points, range_boundaries)
    print("Data Points:", data_points)
    print("Range Boundaries:", range_boundaries)
    print("Bin Labels:", labels)
    print("Bin Indices:", indices)