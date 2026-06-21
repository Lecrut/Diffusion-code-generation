def group_by_bins(data, step_size):
    bins = {}
    for number in data:
        bin_start = (number // step_size) * step_size
        if bin_start not in bins:
            bins[bin_start] = []
        bins[bin_start].append(number)
    return bins

if __name__ == '__main__':
    sample_data = [10, 23, 45, 67, 89, 12, 34, 56, 78]
    step_size = 10
    grouped_bins = group_by_bins(sample_data, step_size)
    print(grouped_bins)