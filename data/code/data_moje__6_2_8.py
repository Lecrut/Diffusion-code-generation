def weight_differences(pairs):
    for weight1, weight2 in pairs:
        yield abs(weight1 - weight2)

if __name__ == '__main__':
    sample_pairs = [(10, 12), (5, 8), (7, 3), (15, 15)]
    differences = list(weight_differences(sample_pairs))
    print(differences)