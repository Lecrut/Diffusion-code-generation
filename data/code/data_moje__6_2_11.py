def weight_differences(weight_pairs):
    for pair in weight_pairs:
        yield pair[0] - pair[1]

if __name__ == '__main__':
    sample_pairs = [
        (80.5, 78.2),
        (65.0, 67.3),
        (90.1, 85.4),
        (72.8, 72.8),
    ]
    differences = list(weight_differences(sample_pairs))
    print(differences)