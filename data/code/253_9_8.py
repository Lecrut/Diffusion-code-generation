def find_the_middle_value_among_three_filter_valid(samples):
    valid_samples = []
    for sample in samples:
        if len(sample) == 3 and all(isinstance(x, (int, float)) for x in sample):
            valid_samples.append(sorted(sample)[1])
    return valid_samples

if __name__ == '__main__':
    samples = [
        [2, 5, 3],
        [4.5, 1.2, 3.7],
        ['a', 2, 3],
        [10, 10, 10]
    ]
    print(find_the_middle_value_among_three_filter_valid(samples))