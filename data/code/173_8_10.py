def group_by_step(data, step):
    if not all(isinstance(x, int) for x in data):
        raise ValueError("Data must contain only integers")
    if not isinstance(step, int) or step <= 0:
        raise ValueError("Step must be a positive integer")

    bins = {}
    for value in data:
        bin_start = (value // step) * step
        bins.setdefault(bin_start, []).append(value)

    return bins

if __name__ == '__main__':
    sample_data = [10, 23, 45, 67, 89, 12]
    step_size = 10
    grouped_data = group_by_step(sample_data, step_size)
    print(grouped_data)