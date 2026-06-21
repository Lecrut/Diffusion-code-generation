def calculate_weight_difference(weights):
    if not weights:
        raise ValueError("The list of weights cannot be empty.")
    
    def find_extremes(lst):
        max_value = lst[0]
        min_value = lst[0]
        for value in lst:
            if value > max_value:
                max_value = value
            if value < min_value:
                min_value = value
        return max_value, min_value
    
    max_weight, min_weight = find_extremes(weights)
    return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [45.6, 78.9, 12.3, 90.2, 34.5]
    difference = calculate_weight_difference(sample_weights)
    print(difference)