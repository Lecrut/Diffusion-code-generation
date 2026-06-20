def calculate_weight_difference(weights):
    if not weights:
        return 0
    max_weight = max(weights)
    min_weight = min(weights)
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [15.5, 3.2, 8.7, 22.1, 4.9, 11.0]
    result = calculate_weight_difference(sample_weights)
    print(result)