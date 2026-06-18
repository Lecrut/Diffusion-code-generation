"""
Module to scale volume data by a given factor with floating-point precision.

This module provides functionality to take an initial list of volumes,
apply a scaling factor to each element, and return a new list containing
the scaled values. It ensures that the calculations maintain standard 
floating-point precision using Python's native float type.
"""

def scale_volumes(volumes: list[float], factor: float) -> list[float]:
    """
    Scale a given list of volumes by a specified factor.

    Args:
        volumes (list[float]): The initial list of volume values to be scaled.
        factor (float): The multiplication factor to apply to each volume.

    Returns:
        list[float]: A new list containing the scaled volume values.
    
    Example:
        >>> scale_volumes([10, 25, 30], 2)
        [20.0, 50.0, 60.0]
    """
    return [v * factor for v in volumes]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    initial_volumes = [10.5, 23.7, 45.2, 67.89]
    scaling_factor = 2.5

    scaled_result = scale_volumes(initial_volumes, scaling_factor)
    
    # Output the result for verification (no interactive prompts used).
    print("Original volumes:", initial_volumes)
    print(f"Scaling factor: {scaling_factor}")
    print("Scaled volumes:", scaled_result)