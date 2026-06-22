def calculate_weight_difference(weights):
    if not weights:
        return 0
    min_weight = weights[0]
    max_weight = weights[0]
    for weight in weights[1:]:
        if weight < min_weight:
            min_weight = weight
        if weight > max_weight:
            max_weight = weight
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [72.5, 68.3, 81.2, 55.0, 90.1, 45.8]
    result = calculate_weight_difference(sample_weights)
    print(result)