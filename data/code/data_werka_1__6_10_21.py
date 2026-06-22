def calculate_weight_difference(weights):
    if not weights:
        return 0
    max_weight = max(weights)
    min_weight = min(weights)
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [23, 45, 67, 89, 12, 34, 56]
    difference = calculate_weight_difference(sample_weights)
    print(difference)