"""
Volume Measurement Comparison Script.

This script defines a function to compare two volume measurements provided as floating-point numbers
and prints the result in a human-readable format. It includes a main block with hard-coded sample values
to demonstrate functionality without requiring any user input or external dependencies.
"""

def compare_volumes(volume_a: float, volume_b: float) -> str:
    """
    Compares two floating-point numbers representing volumes and returns a formatted string result.

    Args:
        volume_a (float): The first volume measurement to be compared.
        volume_b (float): The second volume measurement to be compared.

    Returns:
        str: A human-readable message indicating the relationship between the two volumes.
             - 'Volume A is greater than Volume B' if a > b
             - 'Volumes are equal' if a == b
             - 'Volume B is greater than Volume A' if a < b

    Raises:
        TypeError: If either argument is not a float or int.
    """
    # Ensure inputs are numeric (float or int)
    try:
        value_a = float(volume_a)
        value_b = float(volume_b)
    except (TypeError, ValueError):
        return "Error: Both arguments must be valid numbers."

    if value_a > value_b:
        result_text = f"Volume A ({value_a}) is greater than Volume B ({value_b})."
    elif value_b > value_a:
        result_text = f"Volume B ({value_b}) is greater than Volume A ({value_a})."
    else:
        result_text = "Volumes are equal."

    return result_text

if __name__ == '__main__':
    # Hard-coded sample values for demonstration.
    # No user input, command-line arguments, or network access required.
    
    vol_1 = 50.75      # Sample volume A in liters
    vol_2 = 48.30      # Sample volume B in liters
    
    comparison_result = compare_volumes(vol_1, vol_2)
    
    print(comparison_result)