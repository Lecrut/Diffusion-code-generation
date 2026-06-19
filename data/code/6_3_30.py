def calculate_weight_difference(weights):
    if not weights:
        return 0
    
    min_weight = float('inf')
    max_weight = float('-inf')
    
    for weight in weights:
        if weight < min_weight:
            min_weight = weight
        if weight > max_weight:
            max_weight = weight
    
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [50, 20, 70, 30, 90, 10]
    difference = calculate_weight_difference(sample_weights)
    print(difference)