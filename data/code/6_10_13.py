def calculate_weight_difference(weights):
    if not weights:
        return 0
    max_weight = weights[0]
    min_weight = weights[0]
    for weight in weights:
        if weight > max_weight:
            max_weight = weight
        elif weight < min_weight:
            min_weight = weight
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [12, 45, 7, 99, 34, 78, 12]
    result = calculate_weight_difference(sample_weights)
    print(result)