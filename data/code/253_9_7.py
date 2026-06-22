def find_the_middle_value_among_three_filter_valid(samples):
    valid_samples = []
    for sample in samples:
        try:
            a, b, c = map(int, sample.split())
            if len(set([a, b, c])) == 3:
                valid_samples.append((a, b, c))
        except ValueError:
            continue
    return valid_samples

if __name__ == '__main__':
    samples = [
        "1 2 3",
        "4 5 6",
        "7 8 a",
        "9 10 11"
    ]
    print(find_the_middle_value_among_three_filter_valid(samples))