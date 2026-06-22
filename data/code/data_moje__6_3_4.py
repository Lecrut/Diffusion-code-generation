def weight_difference(weights):
    if not weights:
        return 0
    min_weight = weights[0]
    max_weight = weights[0]
    for weight in weights[1:]:
        if weight < min_weight:
            min_weight = weight
        if weight > max_weight:
            max_weight = weight
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [5, 3, 8, 1, 9, 2]
    print(weight_difference(sample_weights))