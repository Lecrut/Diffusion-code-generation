def find_outliers(weight_entries, min_weight, max_weight):
    outliers = []
    for weight in weight_entries:
        if weight < min_weight or weight > max_weight:
            outliers.append(weight)
    return outliers

if __name__ == '__main__':
    sample_weights = [45, 60, 75, 210, 55, 199, 5, 300, 150]
    result = find_outliers(sample_weights, 50, 200)
    print(result)