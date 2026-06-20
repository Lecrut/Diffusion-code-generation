def weight_difference(weights):
    if not weights:
        return 0
    min_weight = max_weight = weights[0]
    for w in weights[1:]:
        if w < min_weight:
            min_weight = w
        if w > max_weight:
            max_weight = w
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = weight_difference(sample_weights)
    print(result)