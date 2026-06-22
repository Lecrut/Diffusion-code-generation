def find_outlier_weights(weights, min_weight=50.0, max_weight=200.0):
    return [w for w in weights if w < min_weight or w > max_weight]

if __name__ == '__main__':
    sample_weights = [45.0, 100.0, 205.0, 150.0, 201.0, 49.9, 50.0]
    outliers = find_outlier_weights(sample_weights)
    print(outliers)