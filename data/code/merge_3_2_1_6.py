def calculate_average_volume(volumes: list[float]) -> float:
    """
    Calculates the arithmetic mean of a list of volume measurements.
    
    Uses built-in functions (sum) which are implemented in C for maximum efficiency,
    avoiding explicit Python-level loops via list comprehensions or generators where not strictly necessary 
    but sum() is inherently optimized over manual iteration.

    Args:
        volumes (list[float]): A non-empty list of numeric volume measurements.

    Returns:
        float: The arithmetic mean of the provided volume measurements.

    Raises:
        ValueError: If the input list is empty or None.
    
    Examples:
        >>> calculate_average_volume([10, 20, 30])
        20.0
        
        >>> calculate_average_volume([])
        Traceback (most recent call last):
            ...
            ValueError
    """
    if not volumes or len(volumes) == 0:
        raise ValueError("Volume list cannot be empty.")
    
    return sum(volumes) / len(volumes)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or network access used here.
    sample_volumes = [50.5, 102.3, 75.8, 90.1]

    try:
        result = calculate_average_volume(sample_volumes)
        print(f"The average volume is: {result}")
    except ValueError as e:
        # This block handles the error case if an empty list were passed during a real run, 
        # though it won't trigger with the current hardcoded sample.
        print(f"Error occurred: {e}")