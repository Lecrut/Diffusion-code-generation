def calculate_weight_difference(weights):
    if not weights:
        return 0
    max_weight = max(weights)
    min_weight = min(weights)
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [150, 200, 80, 300, 175]
    difference = calculate_weight_difference(sample_weights)
    print(difference)