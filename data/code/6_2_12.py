def weight_difference(pairs):
    for first, second in pairs:
        yield first - second

if __name__ == '__main__':
    sample_pairs = [(100, 50), (200, 150), (75, 25)]
    result = list(weight_difference(sample_pairs))
    print(result)