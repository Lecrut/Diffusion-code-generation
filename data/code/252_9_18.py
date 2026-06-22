def compare_two_simple_quantities_now_filter_valid(samples):
    valid_samples = []
    for sample in samples:
        if isinstance(sample, dict) and 'quantity1' in sample and 'quantity2' in sample:
            try:
                quantity1 = float(sample['quantity1'])
                quantity2 = float(sample['quantity2'])
                if not (isinstance(quantity1, (int, float)) and isinstance(quantity2, (int, float))):
                    continue
                valid_samples.append({'quantity1': quantity1, 'quantity2': quantity2})
            except ValueError:
                continue
    return valid_samples

if __name__ == '__main__':
    samples = [
        {'quantity1': 5, 'quantity2': 3},
        {'quantity1': 'a', 'quantity2': 7},
        {'quantity1': 8.5, 'quantity2': 'b'},
        {'quantity1': 10, 'quantity2': 10}
    ]
    print(compare_two_simple_quantities_now_filter_valid(samples))