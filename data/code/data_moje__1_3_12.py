def identify_out_of_range_weights(weights, min_weight, max_weight):
    return [weight for weight in weights if weight < min_weight or weight > max_weight]

if __name__ == '__main__':
    sample_weights = [45, 60, 150, 205, 49, 200, 210, 50]
    min_acceptable = 50
    max_acceptable = 200
    outliers = identify_out_of_range_weights(sample_weights, min_acceptable, max_acceptable)
    print(outliers)