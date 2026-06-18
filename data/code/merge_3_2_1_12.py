def calculate_average_volume(volumes):
    """
    Calculate the arithmetic mean of a list of volume measurements.
    
    Args:
        volumes (list[float]): A non-empty list containing numeric volume values.
        
    Returns:
        float: The average value of the input list.
        
    Raises:
        ValueError: If the input list is empty or contains non-numeric elements.
    """
    if not isinstance(volumes, list):
        raise TypeError("Input must be a list.")
    
    if len(volumes) == 0:
        raise ValueError("The volume list cannot be empty.")
    
    try:
        # Using sum() and built-in type checking ensures efficiency and correctness.
        total = sum(float(x) for x in volumes)
        average = total / len(volumes)
        return float(average)
    except TypeError as e:
        raise ValueError(f"All elements must be numeric.") from e

if __name__ == '__main__':
    # Hard-coded sample values representing volume measurements.
    sample_volumes = [10, 25, 30, 45, 60]

    try:
        avg_volume = calculate_average_volume(sample_volumes)
        print(f"The average volume is {avg_volume}")
    except Exception as e:
        print(f"An error occurred while calculating the average: {e}")