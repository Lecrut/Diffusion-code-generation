def weight_difference_generator(pairs):
    for first, second in pairs:
        yield first - second

if __name__ == '__main__':
    sample_pairs = [(10, 5), (20, 15), (30, 35), (40, 40)]
    results = list(weight_difference_generator(sample_pairs))
    print(results)