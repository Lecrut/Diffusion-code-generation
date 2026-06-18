"""
Module to compare two volume inputs using type hints and clear logic explanation via docstrings.

This module provides a function that compares two numeric volumes (integers or floats)
and returns a descriptive result indicating whether they are equal, the first is greater,
or the second is greater. It uses Python's typing system for static analysis clarity.
"""

from typing import Union

def compare_volumes(volume_a: float, volume_b: float) -> str:
    """
    Compares two numeric volumes and returns a descriptive string result based on their relationship.

    This function accepts two arguments representing numerical quantities (volumes).
    It evaluates the mathematical comparison between these inputs and categorizes the outcome.
    
    Comparison Logic:
        1. If volume_a is numerically equal to volume_b, return 'Volumes are identical'.
        2. If volume_a is greater than volume_b, return 'Volume A is larger.'.
        3. Otherwise (volume_a < volume_b), return 'Volume B is larger.'.

    Args:
        volume_a (Union[int, float]): The first numeric value to compare against the second volume.
                                      Accepted types are int or float via Union hinting.
        volume_b (Union[int, float]): The second numeric value for comparison. 
                                     Accepts int or float as per type hints.

    Returns:
        str: A string explaining which volume is larger or if they are equal.

    Example usage within a script context without external inputs would be:
        result = compare_volumes(10, 20) # Returns 'Volume B is larger.'
    """
    
    # Perform the comparison logic based on numerical value
    if volume_a == volume_b:
        return "Volumes are identical"
    elif volume_a > volume_b:
        return "Volume A is larger."
    else:
        return "Volume B is larger."

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or CLI args.
    # These are local test cases ensuring the module runs standalone with no network/files dependency.

    val_1 = 500
    val_2 = 750
    
    print(compare_volumes(val_1, val_2))