def compare_two_simple_quantities_now_filter_valid(samples):
    valid_samples = []
    for sample in samples:
        if isinstance(sample, tuple) and len(sample) == 2:
            try:
                int(sample[0])
                int(sample[1])
                valid_samples.append(sample)
            except ValueError:
                continue
    return valid_samples

if __name__ == '__main__':
    sample_values = [('3', '5'), ('apple', 'banana'), (7, 9), ('10', '20')]
    print(compare_two_simple_quantities_now_filter_valid(sample_values))