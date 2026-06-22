def compare_two_simple_quantities_now_filter_valid(samples):
    valid_samples = []
    for sample in samples:
        if isinstance(sample, tuple) and len(sample) == 2:
            try:
                value1, value2 = map(float, sample)
                if value1 >= 0 and value2 >= 0:
                    valid_samples.append((value1, value2))
            except ValueError:
                continue
    return valid_samples

if __name__ == '__main__':
    samples = [
        (3.5, 4.2),
        ('a', 2.1),
        (-1.0, 5.6),
        (7.8, 'b'),
        (0.0, 0.0)
    ]
    valid_samples = compare_two_simple_quantities_now_filter_valid(samples)
    print(valid_samples)