def weight_differences(weight_pairs):
    for first, second in weight_pairs:
        yield first - second

if __name__ == '__main__':
    sample_pairs = [(10, 5), (20, 15), (100, 75), (50, 60)]
    differences = list(weight_differences(sample_pairs))
    print(differences)