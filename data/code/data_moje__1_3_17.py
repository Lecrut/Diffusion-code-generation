def find_out_of_range_weights(weights, min_weight=50, max_weight=200):
    return [w for w in weights if w < min_weight or w > max_weight]

if __name__ == '__main__':
    sample_weights = [45, 55, 100, 205, 150, 30, 180, 210, 60, 40]
    outliers = find_out_of_range_weights(sample_weights)
    print(outliers)