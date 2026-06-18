def find_weight_difference(weights):
    """
    Calculates the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of float/int): List containing numeric weight values.
        
    Returns:
        float or int: The absolute difference between maximum and minimum weights.
                      If input is empty, returns 0.
                      
    Complexity: O(n) time, where n is the number of elements in the list.
                         Only requires one pass to find min and max values simultaneously.
    """
    if not weights:
        return 0
    
    minimum = float('inf')
    maximum = float('-inf')
    
    for weight in weights:
        if weight < minimum:
            minimum = weight
        elif weight > maximum:
            maximum = weight
            
    # Calculate absolute difference (though max will always be >= min)
    return abs(maximum - minimum)

if __name__ == '__main__':
    sample_weights = [5.2, 10.8, 3.4, 7.9, 5.2]
    
    result = find_weight_difference(sample_weights)
    print(f"Difference: {result}")