import math

def convert_to_appropriate_unit(seconds: float) -> tuple[float, str]:
    """
    Converts a given number of seconds into the most appropriate time unit.
    
    Logic hierarchy (descending order):
    1. If total_seconds >= 3600 (>= 1 hour), return hours and 'h' suffix.
       - Uses integer division for clean boundaries if possible, but handles float input gracefully.
    2. Else if total_seconds >= 60 (< 1 hour but >= 1 minute), return minutes and 'm' suffix.
    3. Otherwise (total_seconds < 60), return seconds and 's' suffix.

    Args:
        seconds (float): A non-negative float representing the duration in seconds.

    Returns:
        tuple[float, str]: A tuple containing the converted value as a float 
                          and the corresponding unit string ('h', 'm', or 's').
    
    Examples:
        >>> convert_to_appropriate_unit(7205)
        (1946.3888888888889, 'h')
        >>> convert_to_appropriate_unit(90)
        (1.5, 'm')
        >>> convert_to_appropriate_unit(30)
        (30.0, 's')
    """
    
    # Check for hours first to ensure the largest appropriate unit is used
    if seconds >= 3600:
        return (seconds / 3600.0, "h")
    elif seconds >= 60:
        return (seconds / 60.0, "m")
    else:
        # For less than a minute, the input is already in the most appropriate unit relative to minutes/hours
        return (float(seconds), "s")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    test_cases = [7205.5, 90, 30, 18640, 5]

    for sec in test_cases:
        converted_value, unit_symbol = convert_to_appropriate_unit(sec)
        print(f"{sec} seconds is {converted_value:.2f} {unit_symbol}")