def find_outliers(weights, min_weight, max_weight):
    return [w for w in weights if w < min_weight or w > max_weight]

if __name__ == '__main__':
    sample_weights = [45, 55, 100, 199, 205, 30, 150, 201]
    min_acceptable = 50
    max_acceptable = 200
    result = find_outliers(sample_weights, min_acceptable, max_acceptable)
    print(result)