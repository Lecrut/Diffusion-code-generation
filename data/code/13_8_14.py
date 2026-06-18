import math

def time_zone_difference(offsets):
    """
    Calculates the difference between the latest (maximum) and earliest 
    (minimum) timezone offset from a given list of offsets.

    Args:
        offsets (list[Union[int, float]]): A list representing timezone offsets in hours or minutes.

    Returns:
        Union[float, int]: The absolute time difference in hours between the max and min offsets.
                          If less than one hour apart, returns a fraction of an hour as a decimal.
    
    Raises:
        ValueError: If the input is empty or not iterable.
        TypeError: If elements are not numbers (int/float).
    """
    if not isinstance(offsets, list) or len(offsets) == 0:
        raise ValueError("Input must be a non-empty list of offsets.")

    for i, offset in enumerate(offsets):
        if not isinstance(offset, (int, float)):
            raise TypeError(f"Offset at index {i} is not a number. Expected int or float, got {type(offset).__name__}.")

    max_offset = max(offsets)
    min_offset = min(offsets)

    return abs(max_offset - min_offset)

if __name__ == '__main__':
    # Hard-coded sample values representing timezone offsets relative to UTC (in hours)
    sample_offsets = [-8.0, 5.0, 0.0, -3.5]  # e.g., PST (+/-), EST, GMT, NZST/EST mix
    
    try:
        diff = time_zone_difference(sample_offsets)
        
        if not isinstance(diff, (int, float)):
            print("Error: Difference calculation failed to return a number.")
        else:
            formatted_diff = round(diff, 10) # Ensure clean output for simple integers or decimals
            print(f"The difference between the earliest and latest offset is {formatted_diff} hours.")
    except (ValueError, TypeError) as e:
        print(f"An error occurred during calculation: {e}")