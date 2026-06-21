def group_into_bins(int_list, step_size):
    bins = {}
    for num in int_list:
        bin_start = (num // step_size) * step_size
        if bin_start not in bins:
            bins[bin_start] = []
        bins[bin_start].append(num)
    return bins

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    step_size = 10
    result = group_into_bins(sample_values, step_size)
    print(result)