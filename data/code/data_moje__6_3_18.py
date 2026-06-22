def weight_difference(weights):
    max_weight = weights[0]
    min_weight = weights[0]
    for w in weights[1:]:
        if w > max_weight:
            max_weight = w
        if w < min_weight:
            min_weight = w
    return max_weight - min_weight

if __name__ == '__main__':
    weights = [10, 20, 30, 40, 50]
    result = weight_difference(weights)
    print(result)