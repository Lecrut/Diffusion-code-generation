def calculate_average_volume(volumes):
    """
    Calculates the arithmetic mean of a list of volume measurements.
    
    This function uses Python's built-in sum() and len() functions 
    to compute the average efficiently, which are implemented in C 
    for maximum performance compared to manual loops or explicit list comprehensions 
    that might create intermediate lists unnecessarily.

    Args:
        volumes (list): A list of numeric values representing volume measurements.
        
    Returns:
        float: The arithmetic mean of the provided volumes.
            
    Raises:
        ValueError: If the input list is empty or does not contain numbers.
    """
    if not isinstance(volumes, list) or len(volumes) == 0:
        raise ValueError("Input must be a non-empty list.")
    
    try:
        total_volume = sum(float(volume) for volume in volumes)
        return total_volume / float(len(volumes))
    except TypeError as e:
        raise ValueError(f"All elements in the list must be numeric. Error details: {e}")

if __name__ == '__main__':
    # Hard-coded sample values representing volume measurements (in liters)
    sample_volumes = [10, 25.5, 30, 45.75, 60]

    try:
        average_volume = calculate_average_volume(sample_volumes)
        print(f"The calculated average volume is: {average_volume:.2f}")
    except ValueError as ve:
        print(f"Error during calculation: {ve}")