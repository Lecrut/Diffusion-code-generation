import numpy as np
def bin_data(data, bins):
    if len(bins) < 2:
        return [data]
    lower_bounds = np.array(bins[:-1])
    upper_bounds = np.array(bins[1:])
    bins_data = []
    for i in range(len(lower_bounds)):
        lower = lower_bounds[i]
        upper = upper_bounds[i]
        if i == len(lower_bounds) - 1:
            current_bin = data[i:]
        else:
            current_bin = data[i:i + len(upper_bounds) - len(lower_bounds)]
        if len(current_bin) > 0:
            bins_data.append(current_bin)
    return bins_data
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    bins = [0, 5, 10, 15, 20, 25]
    result = bin_data(data, bins)
    print(result)