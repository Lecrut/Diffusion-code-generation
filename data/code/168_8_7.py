import numpy as np
def bin_data(data, bins):
    if len(data) != len(bins) - 1:
        raise ValueError("The number of data points must be one less than the number of bin edges.")
    bins_edges = np.array(bins)
    labels = []
    for x in data:
        bin_index = np.searchsorted(bins_edges, x, side='right') - 1
        if 0 <= bin_index < len(bins_edges) - 1:
            labels.append(f"{bins_edges[bin_index]} to {bins_edges[bin_index + 1]}")
        else:
            labels.append("Out of bounds")
    return labels
if __name__ == '__main__':
    data_points = [1.2, 5.5, 10.1, 15.0, 22.3, 3.8, 8.9, 1.0, 18.5, 25.0]
    bin_boundaries = [0, 5, 10, 15, 20, 30]
    try:
        result = bin_data(data_points, bin_boundaries)
        for data, result_label in zip(data_points, result):
            print(f"Data point: {data}, Bin: {result_label}")
    except ValueError as e:
        print(f"Error: {e}")