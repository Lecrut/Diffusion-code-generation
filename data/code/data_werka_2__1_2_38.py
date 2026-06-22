def filter_weights(weights, min_weight, max_weight):
    return [weight for weight in weights if weight < min_weight or weight > max_weight]

if __name__ == '__main__':
    sample_weights = [45, 60, 210, 180, 49, 201, 150]
    min_weight = 50
    max_weight = 200
    outliers = filter_weights(sample_weights, min_weight, max_weight)
    print(outliers)