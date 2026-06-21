def group_by_bins(data, bin_size):
    MIN_BIN = 0
    MAX_BIN = max(data) if data else MIN_BIN

    bins = {i: [] for i in range(MIN_BIN, MAX_BIN + bin_size + 1, bin_size)}

    for num in data:
        bin_index = (num - MIN_BIN) // bin_size * bin_size + MIN_BIN
        bins[bin_index].append(num)

    return bins

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    bin_size = 10
    grouped_bins = group_by_bins(sample_data, bin_size)
    print(grouped_bins)