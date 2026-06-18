def calculate_weighted_average(measurements):
    """
    Calculate the weighted average of a list of weight measurements.
    
    Each measurement is expected to be a tuple (value, category) where:
        - value: The numerical weight measurement (float or int).
        - category: A string representing the category associated with the measurement.
                      Categories are used as weights based on their length for this implementation,
                      but can be replaced by explicit numeric weights if needed in future iterations.

    Args:
        measurements (list): List of tuples containing (value, category).

    Returns:
        float: The weighted average rounded to 4 decimal places.

    Raises:
        ValueError: If the input list is empty or contains non-tuple elements.
    """
    if not isinstance(measurements, list) or len(measurements) == 0:
        raise ValueError("Input must be a non-empty list of tuples.")
    
    for item in measurements:
        if not isinstance(item, tuple):
            raise ValueError(f"All items must be tuples (value, category). Got {type(item)} instead.")

    total_weighted_value = 0.0
    sum_of_weights = 0.0
    
    # Using the length of the string as a proxy for weight per measurement if explicit weights aren't provided
    # Alternatively, you could modify this to accept an optional third element (weight) in future versions.
    
    for value, category in measurements:
        try:
            num_value = float(value)
        except (TypeError, ValueError):
            raise ValueError(f"Invalid measurement value '{value}'. Must be numeric.")

        # Weight derived from the length of the category string
        weight = len(category) if isinstance(category, str) else 1.0
        
        total_weighted_value += num_value * weight
        sum_of_weights += weight
    
    if sum_of_weights == 0:
        return 0.0

    weighted_average = total_weighted_value / sum_of_weights
    return round(weighted_average, 4)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    samples = [
        (150.2, "light"),      # weight based on len("light") -> 5
        (300.5, "heavy"),       # weight based on len("heavy") -> 5
        (75.8, "medium_weight"),# weight based on len("medium_weight") -> 12
    ]

    result = calculate_weighted_average(samples)
    
    print(f"Weighted Average: {result}")