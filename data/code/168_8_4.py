import numpy as np
def bin_data(data, bins):
    if not data:
        return []
    bins = np.array(bins)
    if len(bins) < 2:
        return [data]
    labels = []
    for x in data:
        bin_index = np.searchsorted(bins, x, side='right') - 1
        if bin_index >= 0 and bin_index < len(bins) - 1:
            labels.append(f"{bins[bin_index]} to {bins[bin_index+1]}")
        elif x <= bins[0]:
            labels.append(f"Below {bins[0]}")
        elif x >= bins[-1]:
            labels.append(f"Above {bins[-1]}")
        else:
            labels.append("Error")
    return labels
if __name__ == '__main__':
    data_points = [1.2, 5.5, 10.1, 15.0, 22.3, 30.0, 35.5, 40.0]
    range_boundaries = [0, 10, 20, 30, 45]
    result = bin_data(data_points, range_boundaries)
    print(result)