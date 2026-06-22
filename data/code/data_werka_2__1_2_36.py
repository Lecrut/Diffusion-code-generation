def identify_out_of_range_weights(weights, min_weight=50, max_weight=200):
    out_of_range = [weight for weight in weights if weight < min_weight or weight > max_weight]
    return out_of_range

if __name__ == '__main__':
    sample_weights = [45, 60, 210, 75, 80, 205, 90, 49, 201, 150]
    result = identify_out_of_range_weights(sample_weights)
    print(result)