def calculate_weight_difference(weights):
    if not weights:
        return 0
    min_weight = weights[0]
    max_weight = weights[0]
    for weight in weights:
        if weight < min_weight:
            min_weight = weight
        elif weight > max_weight:
            max_weight = weight
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [10, 25, 5, 40, 15]
    result = calculate_weight_difference(sample_weights)
    print(result)