def find_weight_difference(weights):
    """
    Calculate the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of float/int): A non-empty list of numerical values representing weights.
        
    Returns:
        int or float: The absolute difference between the maximum and minimum weights.
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not weights:
        raise ValueError("The list of weights cannot be empty.")

    min_weight = max(weights)  # This runs in O(n) total (one pass for each operation) or can do single pass manually below
    
    # More explicit single-pass approach to guarantee strict O(n) without implicit overheads, 
    # though built-in max/min are also optimized. Let's use a manual loop for clarity and control.
    
    current_min = float('inf')
    current_max = float('-inf')

    for weight in weights:
        if weight < current_min:
            current_min = weight
        if weight > current_max:
            current_max = weight
            
    return abs(current_max - current_min)

if __name__ == '__main__':
    # Sample values hard-coded as per requirements (no user input, network, or files needed)
    sample_weights = [10.5, 23.7, 45.2, 8.9, 60.1]

    try:
        diff = find_weight_difference(sample_weights)
        print(f"Difference between heaviest and lightest weight: {diff}")
    except ValueError as e:
        print(f"Error: {e}")