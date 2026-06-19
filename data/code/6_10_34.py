def calculate_weight_difference(weights):
    max_weight = float('-inf')
    min_weight = float('inf')
    
    for weight in weights:
        if weight > max_weight:
            max_weight = weight
        if weight < min_weight:
            min_weight = weight
    
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [120, 95, 150, 80, 170, 60]
    difference = calculate_weight_difference(sample_weights)
    print(difference)