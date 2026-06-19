def calculate_weight_difference(weights):
    if not weights:
        return 0
    max_weight = max(weights)
    min_weight = min(weights)
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [120, 85, 90, 130, 75, 110]
    difference = calculate_weight_difference(sample_weights)
    print(difference)