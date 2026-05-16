import numpy as np
def bin_data(data, bins):
    if len(bins) < 2:
        return [data]
    bins = np.array(bins)
    if len(bins) != len(data) - 1:
        raise ValueError("Number of bins must be one less than the number of data points.")
    binned_data = []
    for i in range(len(data)):
        lower_bound = bins[i]
        upper_bound = bins[i+1]
        if lower_bound <= data[i] < upper_bound:
            binned_data.append(int(i))
        elif data[i] == upper_bound and i < len(bins) - 1:
            binned_data.append(int(i))
        else:
            binned_data.append(-1)
    return binned_data
if __name__ == '__main__':
    data_points = [1.2, 5.5, 10.1, 15.0, 22.3, 30.0, 35.5, 40.1]
    range_boundaries = [0, 10, 20, 30, 40, 50]
    try:
        result = bin_data(data_points, range_boundaries)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")