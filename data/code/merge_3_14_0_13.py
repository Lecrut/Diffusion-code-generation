"""
Volume Comparison Module

This module defines a function to compare two volume measurements provided as 
floating-point numbers and prints the result in a human-readable format.

It includes a main execution block with hard-coded sample values that run without 
user input, command-line arguments, network access, or pre-existing files.
"""

def compare_volumes(volume_a: float, volume_b: float) -> None:
    """
    Compare two volume measurements and print the result in a human-readable format.

    Args:
        volume_a (float): The first volume measurement.
        volume_b (float): The second volume measurement.

    Returns:
        None: Prints the comparison result to stdout.
    
    Example Output:
        Comparing 50.5 liters with 75.25 kiloliters...
        Volume A is smaller than Volume B by approximately -136894.5 milliliters.
    """
    # Define conversion factors to a common base unit (milliliters) for accurate comparison
    LITERS_TO_ML = 1000.0
    
    ml_a = volume_a * LITERS_TO_ML
    ml_b = volume_b * LITERS_TO_ML

    difference = ml_b - ml_a

    # Determine the relationship between the two volumes
    if abs(difference) < 0.01: 
        print(f"Comparing {volume_a} liters with {volume_b} kiloliters...")
        print("The volumes are approximately equal.")
    elif difference > 0:
        print(f"Comparing {volume_a} liters with {volume_b} kiloliters...")
        print(f"{volume_a} liters is smaller than {volume_b} kiloliters by approximately {difference:.2f} milliliters.")
    else:
        diff_abs = abs(difference)
        print(f"Comparing {volume_a} liters with {volume_b} kiloliters...")
        print(f"{volume_a} liters is larger than {volume_b} kiloliters by approximately {diff_abs:.2f} milliliters.")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    vol_sample_1 = 50.5      # Volume A in liters
    vol_sample_2 = 75.25     # Volume B in kiloliters

    compare_volumes(vol_sample_1, vol_sample_2)