def weight_difference(weights):
    if not weights:
        raise ValueError("List of weights cannot be empty")
    
    max_weight = weights[0]
    min_weight = weights[0]
    
    for weight in weights[1:]:
        if weight > max_weight:
            max_weight = weight
        if weight < min_weight:
            min_weight = weight
            
    return max_weight - min_weight

if __name__ == '__main__':
    weights_list = [10, 4, 22, 35, 11, 8, 19]
    result = weight_difference(weights_list)
    print(result)