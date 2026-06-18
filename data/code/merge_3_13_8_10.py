"""
Module to calculate the difference between the earliest and latest time zone offsets.

This module provides a function that takes a list of time zone offsets (integers or floats),
assumes they are relative to a common reference, and returns the absolute difference
between the maximum and minimum offset in the list. If the list is empty, it returns 0.
"""

def calculate_offset_difference(offsets):
    """
    Calculates the difference between the earliest and latest time zone offset.

    Args:
        offsets (list[int | float]): A list of numerical values representing timezone offsets.
    
    Returns:
        int or float: The absolute difference between the maximum and minimum offset.
                      Returns 0 if the input list is empty.
                      
    Raises:
        TypeError: If an element in the list cannot be converted to a numeric type, 
                   though this function attempts basic validation during conversion.

    Example:
        >>> calculate_offset_difference([0, -5, 3])
        8
        >>> calculate_offset_difference([])
        0
    """
    if not isinstance(offsets, list):
        raise TypeError("Input must be a list.")
    
    # Check for empty list
    if len(offsets) == 0:
        return 0

    try:
        numeric_offsets = [float(o) for o in offsets]
        max_offset = float(max(numeric_offsets))
        min_offset = float(min(numeric_offsets))
        
        difference = abs(max_offset - min_offset)
        # Return as int if the result is a whole number, otherwise return float.
        # This handles cases like 5.0 vs 8 (though mathematically with floats input it might be .0).
        if difference == int(difference):
            return int(difference)
        else:
            return difference
            
    except ValueError as e:
        raise TypeError("All elements in the offset list must be numeric.") from e

if __name__ == '__main__':
    # Hard-coded sample values for testing.
    # Sample 1: Mixed integers and floats representing UTC offsets (e.g., London, New York, Tokyo relative to UTC)
    timezones_sample_1 = [0, -5, 3] 
    
    # Sample 2: An empty list edge case
    timezones_empty_list = []

    print("Sample 1 Calculation:")
    result_1 = calculate_offset_difference(timezones_sample_1)
    print(f"Offsets: {timezones_sample_1}")
    print(f"Difference (Earliest to Latest): {result_1}\n")

    print("Sample 2 Calculation (Empty List):")
    try:
        result_empty = calculate_offset_difference(timezones_empty_list)
        print(f"Offsets: {timezones_empty_list}")
        print(f"Difference: {result_empty}")
    except Exception as ex:
        print(f"Error occurred during calculation of empty list: {ex}")

    # Additional test with negative and positive values to ensure robustness
    timezones_sample_3 = [-12.5, -4.0, 9.75] 
    result_3 = calculate_offset_difference(timezones_sample_3)
    
    print(f"Sample 3 Calculation:")
    print(f"Offsets: {timezones_sample_3}")
    print(f"Difference (Earliest to Latest): {result_3}")