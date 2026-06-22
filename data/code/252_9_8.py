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
    samples = [
        (3, 5),
        ('a', 7),
        (8, 'b'),
        ('9', '10'),
        (11.5, 12.3)
    ]
    result = compare_two_simple_quantities_now_filter_valid(samples)
    print(result)