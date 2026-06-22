def calculate_weight_difference(weights):
    if not weights:
        return 0
    max_weight = max(weights)
    min_weight = min(weights)
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [50, 20, 30, 10, 40]
    difference = calculate_weight_difference(sample_weights)
    print(difference)