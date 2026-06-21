def calculate_weight_difference(weights):
    if not weights:
        raise ValueError("The list of weights cannot be empty.")
    max_weight = max(weights)
    min_weight = min(weights)
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [23.4, 56.7, 12.8, 90.1, 45.6]
    difference = calculate_weight_difference(sample_weights)
    print(difference)