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
        if bin_index < len(upper_bounds) and (x >= lower_bounds[bin_index] if bin_index > 0 else True) and (x <= upper_bounds[bin_index]):
            labels.append(f"{lower_bounds[bin_index]} to {upper_bounds[bin_index]}")
            binned_data.append(x)
        elif bin_index == 0 and x < upper_bounds[0]:
            labels.append(f"Below {upper_bounds[0]}")
            binned_data.append(x)
        elif bin_index == len(upper_bounds) and x > upper_bounds[-1]:
            labels.append(f"Above {upper_bounds[-1]}")
            binned_data.append(x)
        elif bin_index == 0 and x >= upper_bounds[0]:
            labels.append(f"At or above {upper_bounds[0]}")
            binned_data.append(x)
        elif bin_index == len(upper_bounds) and x <= upper_bounds[-1]:
            labels.append(f"At or below {upper_bounds[-1]}")
            binned_data.append(x)
        else:
            labels.append("Uncategorized")
            binned_data.append(x)
    return labels, binned_data
if __name__ == '__main__':
    data_points = [1.2, 5.5, 10.1, 15.0, 22.3, 3.0, 8.8, 11.5]
    range_boundaries = [0, 5, 10, 15, 25]
    labels, binned = bin_data(data_points, range_boundaries)
    print("Data Points:", data_points)
    print("Range Boundaries:", range_boundaries)
    print("Labels:", labels)
    print("Binned Data:", binned)