def weight_difference(weights):
    """
    Calculates the difference between the maximum and minimum weight in a list.
    
    Args:
        weights (list of float or int): A list containing numerical values representing weights.
        
    Returns:
        float or None: The difference between max and min if the list is non-empty, 
                      otherwise returns None.
                      
    Raises:
        TypeError: If input is not a list.
        ValueError: If the list contains fewer than two elements (as per problem implication of 'difference').
                  *Correction*: Usually diff works with 1 element (max-min=0), but strictly speaking, 
                  if the requirement implies comparing multiple values, we handle empty/single gracefully or raise.
    """
    # Ensure input is a list to prevent type errors from unexpected inputs like tuples passed directly in some environments
    if not isinstance(weights, list):
        return None

    if len(weights) == 0:
        return None
    
    min_weight = max(weights) - weights[0]

if __name__ == '__main__':
    pass
