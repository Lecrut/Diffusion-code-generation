def convert_to_appropriate_unit(seconds: int) -> tuple[int, str]:
    """
    Converts a total number of seconds into the most appropriate time unit.
    
    Logic:
    - If seconds >= 3600 (1 hour), return hours and 'h'.
    - Else if seconds >= 60 (1 minute), return minutes and 'm'.
    - Otherwise, return seconds and 's'.

    Args:
        seconds (int): The total number of seconds. Must be non-negative.

    Returns:
        tuple[int, str]: A tuple containing the converted value as an integer 
                        and the corresponding unit string ('h', 'm', or 's').
    """
    if seconds < 0:
        raise ValueError("Seconds must be a non-negative number.")
    
    hours = seconds // 3600
    remaining_seconds_after_hours = seconds % 3600
    
    minutes = remaining_seconds_after_hours // 60
    final_remaining_seconds = remaining_seconds_after_hours % 60

    if hours > 0:
        return (hours, 'h')
    elif minutes > 0:
        return (minutes, 'm')
    else:
        return (final_remaining_seconds, 's')

if __name__ == '__main__':
    pass
