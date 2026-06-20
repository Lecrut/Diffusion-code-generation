def calculate_weight_difference(weights):
    if not weights:
        return 0
    min_weight = max_weight = weights[0]
    for weight in weights[1:]:
        if weight < min_weight:
            min_weight = weight
        elif weight > max_weight:
            max_weight = weight
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [3.5, 1.2, 7.8, 4.3, 2.1]
    result = calculate_weight_difference(sample_weights)
    print(result)