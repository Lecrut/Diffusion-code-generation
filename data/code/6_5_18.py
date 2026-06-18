def weight_difference(weights):
    """
    Calculates the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of float/int): List containing numerical values representing weights.
        
    Returns:
        float or int: The difference between the maximum and minimum value in the list.
                      Raises ValueError if the input is empty.
                      
    Time Complexity: O(n) - Single pass through the list to find min and max.
    Space Complexity: O(1) - Only uses constant extra space for tracking min/max.
    """
    if not weights:
        raise ValueError("The weight list cannot be empty.")

    # Initialize both minimum and maximum with the first element
    current_min = float('inf')
    current_max = float('-inf')

    for w in weights:
        if w < current_min:
            current_min = w
        elif w > current_max:
            current_max = w
            
    return current_max - current_min

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files)
    sample_weights = [85.2, 40.1, 92.7, 35.6, 88.9]

    try:
        diff = weight_difference(sample_weights)
        print(f"The difference between the heaviest and lightest weight is: {diff}")
    except ValueError as e:
        print(f"Error: {e}")