import statistics

def calculate_weight_difference(weights):
    """
    Calculates the difference between the maximum and minimum weight in a list.
    
    Args:
        weights (list of float or int): A non-empty list containing numerical values representing weights.
        
    Returns:
        float: The difference between the maximum and minimum value in the list.
        
    Raises:
        ValueError: If the input list is empty.
        TypeError: If any element in the list is not a number.
    """
    if len(weights) == 0:
        raise ValueError("The weights list cannot be empty.")
    
    # Using min and max functions which are implemented in C for efficiency, 
    # making this O(n) operation suitable for large lists.
    return float(max(weights)) - float(min(weights))

if __name__ == '__main__':
    sample_weights = [70.5, 82.3, 69.1, 94.0, 77.8]
    
    result = calculate_weight_difference(sample_weights)
    print(f"Difference between max and min weight: {result}")