def calculate_weight_difference(weights):
    if not weights:
        return 0
    max_weight = weights[0]
    min_weight = weights[0]
    for w in weights[1:]:
        if w > max_weight:
            max_weight = w
        elif w < min_weight:
            min_weight = w
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [10, 25, 3, 42, 18, 7, 55, 2]
    result = calculate_weight_difference(sample_weights)
    print(result)