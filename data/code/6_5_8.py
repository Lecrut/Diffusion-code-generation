def weight_difference(weights):
    """
    Calculate the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of float or int): List containing numerical values representing weights.
        
    Returns:
        float or int: The difference between the maximum and minimum weight, or None if input is empty.
    """
    if not weights:
        return None
    
    min_weight = max(weights)  # Initialize both to cover all elements in one pass logic implicitly via Python's built-in which are O(n)
    
    for w in weights:
        if w < min_weight:
            min_weight = w
            
    max_weight = float('-inf')
    for w in weights:
        if w > max_weight:
            max_weight = w
    
    return round(max_weight - min_weight, 2)

if __name__ == '__main__':
    sample_weights = [10.5, 4.3, 8.9, 12.1, 6.7]
    
    result = weight_difference(sample_weights)
    
    print(f"Heaviest: {max(sample_weights)}")
    print(f"Lightest: {min(sample_weights)}")
    print(f"Difference: {result}")