def bin_integers(int_list, step_size):
    bins = {}
    for num in int_list:
        bin_start = (num // step_size) * step_size
        if bin_start not in bins:
            bins[bin_start] = []
        bins[bin_start].append(num)
    return bins

if __name__ == '__main__':
    sample_integers = [10, 23, 45, 67, 89, 100, 123]
    step_size = 20
    print(bin_integers(sample_integers, step_size))