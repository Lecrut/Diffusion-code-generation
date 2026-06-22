def calculate_weight_difference(weights):
    if not weights:
        raise ValueError("The list of weights cannot be empty.")
    
    def find_extremes(lst):
        max_val = lst[0]
        min_val = lst[0]
        for weight in lst:
            if weight > max_val:
                max_val = weight
            if weight < min_val:
                min_val = weight
        return max_val, min_val
    
    max_weight, min_weight = find_extremes(weights)
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [10.5, 20.3, 5.7, 40.2, 25.8]
    difference = calculate_weight_difference(sample_weights)
    print(difference)