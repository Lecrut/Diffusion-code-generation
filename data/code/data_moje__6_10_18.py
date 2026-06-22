def weight_diff(weights):
    min_w = weights[0]
    max_w = weights[0]
    for w in weights:
        if w < min_w:
            min_w = w
        if w > max_w:
            max_w = w
    return max_w - min_w

if __name__ == '__main__':
    weights = [10, 5, 20, 15, 30, 5]
    result = weight_diff(weights)
    print(result)