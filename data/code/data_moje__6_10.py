def weight_difference(weights):
    if not weights:
        return 0
    max_w = weights[0]
    min_w = weights[0]
    for w in weights:
        if w > max_w:
            max_w = w
        if w < min_w:
            min_w = w
    return max_w - min_w

if __name__ == '__main__':
    sample_weights = [10, 5, 20, 15, 8]
    result = weight_difference(sample_weights)
    print(result)