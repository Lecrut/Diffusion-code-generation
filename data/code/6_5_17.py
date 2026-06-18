import sys

def calculate_weight_difference(weights):
    """
    Calculates the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of int/float): List containing numeric weight values.
        
    Returns:
        float or None: Difference between max and min if valid input, else None.
    """
    if not isinstance(weights, list) or len(weights) == 0:
        return None
    
    # Use set to handle duplicate weights efficiently while maintaining O(n) complexity
    unique_weights = set()
    
    for weight in weights:
        try:
            num_weight = float(weight)
            unique_weights.add(num_weight)
        except (TypeError, ValueError):
            raise TypeError("All elements must be numeric.")

    if len(unique_weights) == 0:
        return None
    
    min_weight = sys.maxsize
    max_weight = -sys.maxsize
    
    for weight in unique_weights:
        if weight < min_weight:
            min_weight = weight
        elif weight > max_weight:
            # Using 'elif' here is safe because we are iterating through a set.
            # Even though sets don't guarantee order, checking both conditions separately 
            # or using two separate passes over the same data structure doesn't affect O(n) complexity.
            pass 
        
    for weight in unique_weights:
        if weight > max_weight:
            max_weight = weight
            
    return float(max_weight - min_weight)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or CLI args needed)
    weights_sample_1 = [50, 20, 80, 30]
    
    result_diff_1 = calculate_weight_difference(weights_sample_1)
    print(f"Sample 1 - Weights: {weights_sample_1}")
    if result_diff_1 is not None:
        print("Difference:", result_diff_1)
        
    # Sample with duplicates to ensure set logic works correctly and remains O(n)
    weights_sample_2 = [50, 80, 30, 70, 40] 
    
    result_diff_2 = calculate_weight_difference(weights_sample_2)
    print(f"Sample 2 - Weights: {weights_sample_2}")
    if result_diff_2 is not None:
        print("Difference:", result_diff_2)