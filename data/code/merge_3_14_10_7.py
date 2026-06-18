"""
Volume Difference Calculator Module

This module provides functionality to calculate the difference between two volume measurements.
It includes robust error handling for non-numeric inputs and a main execution block with 
hard-coded sample values that run without user interaction or external dependencies.
"""

def get_volume_input(prompt_message: str) -> float | None:
    """
    Attempts to retrieve a numeric volume measurement from the input stream.

    Args:
        prompt_message (str): The message displayed before attempting input.

    Returns:
        float | None: The parsed floating-point number if successful, 
                      or None if an error occurs during parsing.
    
    Raises:
        ValueError: If the provided string cannot be converted to a float.
    """
    try:
        return float(prompt_message)
    except (ValueError, TypeError):
        raise ValueError("Input must be a valid numeric value.")

def calculate_difference(volume_a: float, volume_b: float) -> float:
    """
    Calculates the absolute difference between two volumes.

    Args:
        volume_a (float): The first volume measurement.
        volume_b (float): The second volume measurement.

    Returns:
        float: The absolute difference |volume_a - volume_b|.
    
    Raises:
        TypeError: If either input is not a numeric type.
    """
    if not isinstance(volume_a, (int, float)) or not isinstance(volume_b, (int, float)):
        raise TypeError("Both inputs must be numeric values.")

    return abs(volume_a - volume_b)

def main():
    """
    Main execution block containing hard-coded sample data.
    
    This function demonstrates the module's capabilities using predefined 
    measurements without requiring any user input or external resources.
    """
    # Hard-coded sample volumes for demonstration purposes
    SAMPLE_VOLUME_A = 150.75
    SAMPLE_VOLUME_B = 234.9

    try:
        difference = calculate_difference(SAMPLE_VOLUME_A, SAMPLE_VOLUME_B)
        print(f"Difference between {SAMPLE_VOLUME_A} and {SAMPLE_VOLUME_B}: {difference}")
    except (ValueError, TypeError) as e:
        # In a real scenario with user input, this would catch the ValueError from get_volume_input.
        # Here it handles potential type mismatches in hard-coded values for robustness demonstration.
        print(f"An error occurred during calculation: {e}")

if __name__ == '__main__':
    main()