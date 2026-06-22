def calculate_weight_difference(weights):
    if not weights:
        raise ValueError("The list of weights cannot be empty.")
    
    def validate_weights(lst):
        if not all(isinstance(weight, (int, float)) for weight in lst):
            raise ValueError("All elements in the list must be numbers.")
    
    validate_weights(weights)
    
    max_weight = max(weights)
    min_weight = min(weights)
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [78.5, 23.4, 67.8, 12.9, 45.6]
    difference = calculate_weight_difference(sample_weights)
    print(difference)