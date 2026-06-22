def weight_difference(weights):
    if not weights:
        return 0
    max_w = weights[0]
    min_w = weights[0]
    for w in weights[1:]:
        if w > max_w:
            max_w = w
        elif w < min_w:
            min_w = w
    return max_w - min_w

if __name__ == '__main__':
    sample_weights = [10, 5, 8, 20, 15, 3, 7]
    print(weight_difference(sample_weights))