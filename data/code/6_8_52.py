def calculate_weight_difference(weights):
    if not isinstance(weights, list):
        raise ValueError("Input must be a list.")
    if not weights:
        raise ValueError("The list of weights cannot be empty.")
    
    def find_extremes(lst):
        max_val = float('-inf')
        min_val = float('inf')
        for weight in lst:
            if weight > max_val:
                max_val = weight
            if weight < min_val:
                min_val = weight
        return max_val, min_val
    
    max_weight, min_weight = find_extremes(weights)
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [78.9, 23.4, 56.1, 12.0, 90.3]
    difference = calculate_weight_difference(sample_weights)
    print(difference)