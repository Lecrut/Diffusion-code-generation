def max_minus_min(weights):
    min_val = weights[0]
    max_val = weights[0]
    for w in weights:
        if w < min_val:
            min_val = w
        elif w > max_val:
            max_val = w
    return max_val - min_val

if __name__ == '__main__':
    weights = [10, 5, 8, 12, 3, 7]
    result = max_minus_min(weights)
    print(result)