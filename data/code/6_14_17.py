import statistics

def weight_range(weights):
    """
    Calculates the difference between the maximum and minimum weight in a list.
    
    Args:
        weights (list of float or int): A non-empty list containing numerical values representing weights.
        
    Returns:
        float: The range (max - min) of the weights.
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not weights:
        raise ValueError("The weight list cannot be empty.")
    
    # Using max() and min() directly on a generator expression or simple iteration 
    # avoids creating intermediate lists, which improves memory efficiency for large datasets.
    return float(max(weights) - min(weights))

if __name__ == '__main__':
    sample_weights = [10.5, 23.4, 89.1, 5.6, 78.9]
    
    try:
        result = weight_range(sample_weights)
        print(f"The difference between the maximum and minimum weight is: {result}")
    except ValueError as e:
        print(f"Error: {e}")