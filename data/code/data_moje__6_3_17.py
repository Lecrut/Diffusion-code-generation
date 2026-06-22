def weight_difference(weights):
    if not weights:
        return 0
    max_weight = weights[0]
    min_weight = weights[0]
    for w in weights[1:]:
        if w > max_weight:
            max_weight = w
        if w < min_weight:
            min_weight = w
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [3.5, 1.2, 7.8, 4.1, 2.3]
    print(weight_difference(sample_weights))