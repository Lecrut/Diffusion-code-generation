def calculate_weight_difference(weights):
    if not weights:
        raise ValueError("The list of weights cannot be empty.")
    
    def validate_weights(lst):
        for weight in lst:
            if not isinstance(weight, (int, float)):
                raise ValueError("All elements in the list must be numbers.")
    
    validate_weights(weights)
    
    max_weight = max(weights)
    min_weight = min(weights)
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [10.5, 20.3, 5.7, 40.8, 25.6]
    difference = calculate_weight_difference(sample_weights)
    print(difference)