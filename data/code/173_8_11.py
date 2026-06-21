def bin_grouping(data, step_size):
    bins = {}
    for number in data:
        bin_key = (number // step_size) * step_size
        if bin_key not in bins:
            bins[bin_key] = []
        bins[bin_key].append(number)
    return bins

if __name__ == '__main__':
    sample_data = [10, 23, 45, 67, 89, 12, 34, 56]
    step_size = 10
    result = bin_grouping(sample_data, step_size)
    print(result)