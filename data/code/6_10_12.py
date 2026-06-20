def weight_difference(weights):
    min_weight = weights[0]
    max_weight = weights[0]
    for weight in weights:
        if weight < min_weight:
            min_weight = weight
        if weight > max_weight:
            max_weight = weight
    return max_weight - min_weight

if __name__ == '__main__':
    weights_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    result = weight_difference(weights_list)
    print(result)