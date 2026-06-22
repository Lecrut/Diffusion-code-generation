def compare_two_simple_quantities_now_filter_valid(samples):
    valid_samples = []
    for sample in samples:
        try:
            value = float(sample)
            if value >= 0:
                valid_samples.append(value)
        except ValueError:
            continue
    return valid_samples

if __name__ == '__main__':
    samples = ['123', '45.67', '-89', 'abc', '0']
    print(compare_two_simple_quantities_now_filter_valid(samples))