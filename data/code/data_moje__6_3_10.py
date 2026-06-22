def max_min_diff(weights):
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
    weights_list = [10, 3, 5, 8, 12, 2]
    result = max_min_diff(weights_list)
    print(result)