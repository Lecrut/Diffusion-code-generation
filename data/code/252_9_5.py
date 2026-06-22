def compare_two_simple_quantities_now_filter_valid(samples):
    valid_samples = []
    for sample in samples:
        if isinstance(sample, dict) and 'quantity' in sample and 'unit' in sample:
            try:
                quantity = float(sample['quantity'])
                if quantity >= 0:
                    valid_samples.append(sample)
            except ValueError:
                continue
    return valid_samples

if __name__ == '__main__':
    samples = [
        {'quantity': '10', 'unit': 'kg'},
        {'quantity': '-5', 'unit': 'kg'},
        {'quantity': '2.5', 'unit': 'kg'},
        {'quantity': 'apple', 'unit': 'kg'}
    ]
    valid_samples = compare_two_simple_quantities_now_filter_valid(samples)
    print(valid_samples)