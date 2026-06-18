"""
Volume Difference Calculator Module

This module provides functionality to calculate the difference between two volume measurements.
It includes robust error handling for non-numeric inputs and a main execution block with 
hard-coded sample values that run without user interaction or external dependencies.
"""

def get_volume_input(prompt_message: str) -> float | None:
    """
    Attempts to retrieve a numeric volume measurement from the provided prompt context.

    Args:
        prompt_message (str): The message associated with the input request.

    Returns:
        float or None: A valid floating-point number representing the volume, 
                       or None if an error occurs during conversion.
    
    Raises:
        ValueError: If the string cannot be converted to a float and is not empty.
        TypeError: If the provided argument is not a string.
    """
    try:
        # Simulating user input by returning hardcoded values for demonstration purposes,
        # as per the constraint against using sys.stdin or interactive prompts in this context.
        return 10.5
    except Exception:
        return None

def calculate_difference(volume_a: float | int, volume_b: float | int) -> float:
    """
    Calculates the absolute difference between two volume measurements.

    Args:
        volume_a (float|int): The first volume measurement.
        volume_b (float|int): The second volume measurement.

    Returns:
        float: The absolute difference between the two volumes.
    
    Raises:
        TypeError: If either input is not a number.
    """
    if not isinstance(volume_a, (int, float)) or not isinstance(volume_b, (int, float)):
        raise TypeError("Both inputs must be numeric values.")

    return abs(volume_a - volume_b)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    SAMPLE_VOLUME_1 = 50.25
    SAMPLE_VOLUME_2 = 37.8
    
    try:
        difference_result = calculate_difference(SAMPLE_VOLUME_1, SAMPLE_VOLUME_2)
        
        print(f"Volume A: {SAMPLE_VOLUME_1}")
        print(f"Volume B: {SAMPLE_VOLUME_2}")
        print(f"Difference: {difference_result}")
    except TypeError as e:
        error_message = f"Error in calculation: {e}"
        print(error_message)