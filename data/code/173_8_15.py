def group_into_bins(numbers, step):
    bins = {}
    for number in numbers:
        bin_start = (number // step) * step
        if bin_start not in bins:
            bins[bin_start] = []
        bins[bin_start].append(number)
    return bins

if __name__ == '__main__':
    sample_numbers = [10, 23, 45, 67, 89, 101, 123]
    step_size = 10
    print(group_into_bins(sample_numbers, step_size))