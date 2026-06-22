def weight_difference(weights):
    if not weights:
        raise ValueError("List must not be empty")
    max_weight = weights[0]
    min_weight = weights[0]
    for w in weights:
        if w > max_weight:
            max_weight = w
        if w < min_weight:
            min_weight = w
    return max_weight - min_weight

if __name__ == '__main__':
    weights = [50, 10, 80, 30, 60]
    result = weight_difference(weights)
    print(result)