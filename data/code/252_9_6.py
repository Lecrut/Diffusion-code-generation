def compare_two_simple_quantities_now_filter_valid(samples):
    valid_samples = []
    for sample in samples:
        if isinstance(sample, (int, float)) and sample >= 0:
            valid_samples.append(sample)
    return valid_samples

if __name__ == '__main__':
    samples = [1, -2, 3.5, 'a', None, 4]
    print(compare_two_simple_quantities_now_filter_valid(samples))