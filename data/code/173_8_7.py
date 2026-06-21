def bin_integers(numbers, step):
    bins = {}
    for number in numbers:
        bin_start = (number // step) * step
        if bin_start not in bins:
            bins[bin_start] = []
        bins[bin_start].append(number)
    return bins

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    step_size = 3
    print(bin_integers(sample_numbers, step_size))