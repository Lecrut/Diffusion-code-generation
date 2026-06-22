def compare_two_simple_quantities_now_filter_valid(a, b):
    if a is None or b is None:
        return None
    return (a, b) if a <= b else (b, a)

if __name__ == '__main__':
    sample1 = (3, 5)
    sample2 = (7, 2)
    sample3 = (4, 4)
    samples = [sample1, sample2, sample3]
    valid_samples = [compare_two_simple_quantities_now_filter_valid(a, b) for a, b in samples if compare_two_simple_quantities_now_filter_valid(a, b)]
    print(valid_samples)