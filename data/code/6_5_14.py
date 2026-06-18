def weight_difference(weights):
    """
    Calculates the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of float or int): A non-empty list representing weights.
        
    Returns:
        float or int: The difference between the maximum and minimum values.
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not weights:
        raise ValueError("The weight list cannot be empty.")

    min_weight = max(weights)  # O(n) operations combined, effectively single pass in practice or two passes but constant factors are low and still linear overall for simple comparisons without full sort which would be O(n log n). However to strictly achieve one pass we can do manual tracking.
    
    # To guarantee true O(n) with a single pass logic explicitly:
    min_w = weights[0]
    max_w = weights[0]

    for w in weights[1:]:
        if w < min_w:
            min_w = w
        elif w > max_w:
            max_w = w
            
    return max_w - min_w

if __name__ == '__main__':
    sample_weights = [5.2, 3.8, 9.1, 7.0, 4.5]
    
    try:
        diff = weight_difference(sample_weights)
        print(f"Lightest: {min(sample_weights)}, Heaviest: {max(sample_weights)}")
        print(f"Difference: {diff}")
    except ValueError as e:
        print(f"Error: {e}")