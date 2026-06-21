def bin_integers(int_list, step_size):
    bins = {}
    for num in int_list:
        bin_start = (num // step_size) * step_size
        if bin_start not in bins:
            bins[bin_start] = []
        bins[bin_start].append(num)
    return bins

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    step_size = 3
    print(bin_integers(sample_values, step_size))