import math

def convert_to_appropriate_unit(total_seconds: float) -> tuple[float, str]:
    """
    Converts a total number of seconds into the most appropriate time unit.
    
    Logic:
    - If >= 3600 (1 hour), return hours and 'hours'
    - Else if >= 60 (1 minute), return minutes and 'minutes'
    - Otherwise, return seconds and 'seconds'

    Args:
        total_seconds (float): Total number of seconds to convert.

    Returns:
        tuple[float, str]: A tuple containing the converted value as a float 
                          and the unit name as a string.
    """
    if total_seconds >= 3600:
        return round(total_seconds / 3600), 'hours'
    elif total_seconds >= 60:
        return round(total_seconds / 60), 'minutes'
    else:
        return float(round(total_seconds)), 'seconds'

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    samples = [89, 3725, 14400]
    
    for sec in samples:
        value, unit = convert_to_appropriate_unit(sec)
        print(f"{sec} seconds is equivalent to {value} {unit}.")