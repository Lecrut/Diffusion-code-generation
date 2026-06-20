def calculate_weight_difference(weights):
    if not weights:
        return 0
    return max(weights) - min(weights)

if __name__ == '__main__':
    sample_weights = [150, 200, 175, 120, 190, 160]
    result = calculate_weight_difference(sample_weights)
    print(result)