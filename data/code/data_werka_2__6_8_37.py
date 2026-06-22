def calculate_weight_difference(weights):
    if not weights:
        raise ValueError("The list of weights cannot be empty.")
    
    def find_extremes(lst):
        return max(lst), min(lst)
    
    max_weight, min_weight = find_extremes(weights)
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [15.2, 34.7, 89.6, 12.3, 56.4]
    difference = calculate_weight_difference(sample_weights)
    print(difference)