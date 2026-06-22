def compare_two_simple_quantities_now_filter_valid(samples):
    valid_samples = []
    for sample in samples:
        if isinstance(sample, tuple) and len(sample) == 2 and all(isinstance(x, (int, float)) for x in sample):
            valid_samples.append(sample)
    return valid_samples

if __name__ == '__main__':
    sample_values = [(1, 2), 'a', (3.5, 4.5), (5,), (6, 7, 8)]
    print(compare_two_simple_quantities_now_filter_valid(sample_values))