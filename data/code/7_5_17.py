def convert_to_appropriate_unit(total_seconds: int) -> tuple[int, str]:
    """
    Converts a total number of seconds into the most appropriate time unit.
    
    The logic prioritizes larger units to minimize fractional parts in the output value:
    1. If total_seconds >= 3600 (1 hour), returns hours and 'hours'.
    2. Else if total_seconds >= 60 (1 minute), returns minutes and 'minutes'.
    3. Otherwise, returns seconds as an integer and 'seconds'.

    Args:
        total_seconds (int): The number of input seconds to convert. Must be non-negative.

    Returns:
        tuple[int, str]: A tuple containing the converted value in the appropriate unit 
                        and a string representing that unit name ('hours', 'minutes', or 'seconds').
    
    Raises:
        ValueError: If total_seconds is negative.
    """
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative.")

    # Check for hours (3600 seconds)
    if total_seconds >= 3600:
        return total_seconds // 3600, "hours"
    
    # Check for minutes (60 seconds)
    elif total_seconds >= 60:
        return total_seconds // 60, "minutes"
    
    # Default to seconds
    else:
        return int(total_seconds), "seconds"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    test_cases = [86400, 3700, 125, 90]

    print("Conversion Results:")
    for seconds in test_cases:
        value, unit_name = convert_to_appropriate_unit(seconds)
        print(f"{seconds} total seconds -> {value} {unit_name}")