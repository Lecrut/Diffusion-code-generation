def calculate_weight_difference(weights):
    if not weights:
        raise ValueError("The list of weights cannot be empty.")
    
    def find_max(lst):
        max_val = lst[0]
        for val in lst:
            if val > max_val:
                max_val = val
        return max_val
    
    def find_min(lst):
        min_val = lst[0]
        for val in lst:
            if val < min_val:
                min_val = val
        return min_val
    
    max_weight = find_max(weights)
    min_weight = find_min(weights)
    
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [78.5, 23.4, 90.1, 12.3, 67.8]
    difference = calculate_weight_difference(sample_weights)
    print(difference)