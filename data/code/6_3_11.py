def weight_difference(weights):
    if not weights:
        return 0
    min_weight = weights[0]
    max_weight = weights[0]
    for weight in weights:
        if weight < min_weight:
            min_weight = weight
        if weight > max_weight:
            max_weight = weight
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [10.5, 15.2, 8.3, 20.1, 12.7]
    result = weight_difference(sample_weights)
    print(result)