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
    """
    if not weights:
        raise ValueError("The list of weights cannot be empty.")
    
    # Using max() and min() functions which are implemented in C for high performance on large lists,
    # making this approach highly efficient compared to manual iteration or sorting the entire list.
    return float(max(weights) - min(weights))

if __name__ == '__main__':
    sample_weights = [10.5, 23.4, 89.7, 56.2, 12.1]
    
    try:
        diff = calculate_weight_difference(sample_weights)
        print(f"Difference between max and min weight: {diff}")
    except ValueError as e:
        print(f"Error: {e}")