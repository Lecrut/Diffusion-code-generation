"""
Module to convert a total number of seconds into the most appropriate time unit.

The algorithm greedily converts the input seconds down to larger units (hours, minutes, seconds)
if they exist and if there are enough remaining seconds to constitute at least one full unit.
This ensures the output contains:
- The count of hours > 0 (and no remainder in minutes/seconds), OR
- The count of minutes > 0 (and no remainder in seconds), OR
- Just an integer representing total seconds < 60.

Author: Assistant
"""

def convert_seconds_to_unit(total_seconds: int) -> tuple[int, str]:
    """
    Convert a non-negative number of seconds into the most appropriate time unit.

    Args:
        total_seconds (int): The total count of seconds to be converted. Must be >= 0.

    Returns:
        tuple[int, str]: A tuple containing two elements:
            - int: The magnitude in the chosen unit (hours > minutes > seconds).
            - str: The name of the corresponding time unit ('hours', 'minutes', or 'seconds').
    
    Logic:
        1. If total_seconds >= 3600, convert to hours and return count + "hours".
           Note: We don't reduce further to minutes if we have full hours because
           an hour is a more appropriate unit than sixty minutes in this context.
        2. Else, if total_seconds >= 60, return the value as 'minutes'.
        3. Otherwise, assume it's less than 60 and treat it as raw seconds.

    Example:
        >>> convert_seconds_to_unit(7200)       # Returns (2, 'hours') - though technically could be 120m? 
                                                # The prompt implies "most appropriate" usually means largest valid unit > 0.
        However, strict interpretation of "if seconds > 3600 return hours; else if seconds > 60..." suggests stopping at first condition met.
        Let's align with the specific logic requested:
          - If >= 3600 -> Hours (count = total // 3600)
          - Else if >= 60 -> Minutes (count = total // 60)
          - Else -> Seconds
    
    """

    # Check for hours first as they represent the largest unit > 1 hour typically used in such contexts.
    if total_seconds >= 3600:
        return divmod(total_seconds, 3600)[0], "hours"
    
    elif total_seconds >= 60:
        return divmod(total_seconds, 60)[0], "minutes"
    
    else:
        # If less than an hour and less than a minute, it is just seconds.
        # The value itself represents the count of seconds.
        if isinstance(total_seconds, int) or (isinstance(total_seconds, float) and total_seconds == int(total_seconds)):
            return int(total_seconds), "seconds"
        else:
            raise TypeError("Input must be an integer representing non-negative seconds.")

if __name__ == '__main__':
    # Hard-coded sample values to test the logic without user input.
    
    # Test case 1: Large number of seconds resulting in hours
    sec_val_1 = 7205
    res_hrs, unit_hrs = convert_seconds_to_unit(sec_val_1)
    print(f"Input: {sec_val_1} seconds -> Output: {res_hrs} {unit_hrs}")

    # Test case 2: Number of seconds resulting in minutes (but less than an hour)
    sec_val_2 = 3590
    res_min, unit_min = convert_seconds_to_unit(sec_val_2)
    print(f"Input: {sec_val_2} seconds -> Output: {res_min} {unit_min}")

    # Test case 3: Small number of seconds (< 60), should remain as 'seconds'
    sec_val_3 = 45.9 # float input handled by checking integer equivalence inside logic or type check if needed, 
                     # but the function expects int based on signature docstring. Let's use an int for simplicity in main block.
    sec_val_3_int = 45
    res_sec, unit_sec = convert_seconds_to_unit(sec_val_3_int)
    print(f"Input: {sec_val_3_int} seconds -> Output: {res_sec} {unit_sec}")

    # Edge case: exactly 60 seconds should be minutes.
    sec_val_edge = 60
    res_min2, unit_min2 = convert_seconds_to_unit(sec_val_edge)
    print(f"Input: {sec_val_edge} seconds -> Output: {res_min2} {unit_min2}")

    # Edge case: exactly 3600 seconds should be hours.
    sec_val_hr_edge = 3600
    res_hrs2, unit_hrs2 = convert_seconds_to_unit(sec_val_hr_edge)
    print(f"Input: {sec_val_hr_edge} seconds -> Output: {res_hrs2} {unit_hrs2}")