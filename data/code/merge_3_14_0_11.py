"""
Module to compare two volume measurements provided as floating-point numbers 
and print the result in a human-readable format.

This script defines a function that takes two float values representing volumes,
compares them, and outputs which is larger along with their difference.
No user input or external dependencies are required for execution.
"""

def compare_volumes(volume_a: float, volume_b: float) -> None:
    """
    Compare two volume measurements.

    Args:
        volume_a (float): The first volume measurement.
        volume_b (float): The second volume measurement.

    Returns:
        None: Prints the comparison result to standard output.
    
    Examples:
        >>> compare_volumes(50, 75)
        "Volume B is larger by 25.0 units."
        
        >>> compare_volumes(100.5, 100.5)
        "Both volumes are equal."
    """
    
    # Determine the greater value and calculate the difference magnitude
    if volume_a > volume_b:
        larger_vol = volume_a
        smaller_vol = volume_b
    elif volume_b > volume_a:
        larger_vol = volume_b
        smaller_vol = volume_a
    else:
        print("Both volumes are equal.")
        return

    # Calculate the absolute difference between the two volumes
    diff_value = abs(volume_a - volume_b)

    # Generate and print a human-readable message describing the comparison result
    if larger_vol == volume_a:
        print(f"Volume A is {diff_value} greater than Volume B.")
    else:
        print(f"Volume B is {diff_value} greater than Volume A.")

if __name__ == '__main__':
    # Hard-coded sample values for testing execution without user input or network access.
    val_1 = 42.50
    val_2 = 78.9
    
    print("--- Starting Volume Comparison ---")
    compare_volumes(val_1, val_2)