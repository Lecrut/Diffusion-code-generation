def weight_difference_generator(pairs):
    for first, second in pairs:
        yield second - first

if __name__ == '__main__':
    sample_pairs = [(70, 75), (80, 78), (65, 70), (90, 95)]
    results = list(weight_difference_generator(sample_pairs))
    print(results)