def calculate_weight_difference(weights):
    if not weights:
        return 0
    max_weight = float('-inf')
    min_weight = float('inf')
    for weight in weights:
        if weight > max_weight:
            max_weight = weight
        if weight < min_weight:
            min_weight = weight
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [120, 85, 90, 200, 75, 150]
    difference = calculate_weight_difference(sample_weights)
    print(difference)