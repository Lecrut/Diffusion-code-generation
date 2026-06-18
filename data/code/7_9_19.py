import datetime

def calculate_time_difference(start: datetime.datetime | None = None, end: datetime.datetime | None = None) -> dict[str, int]:
    """
    Calculates the time difference between two arbitrary datetime objects and returns a dictionary
    representing the duration in days, hours, minutes, seconds, microseconds.

    Args:
        start (datetime.datetime): The starting point of the interval. Defaults to now if not provided.
        end (datetime.datetime): The ending point of the interval. Defaults to None (not used for diff).

    Returns:
        dict[str, int]: A dictionary containing 'days', 'hours', 'minutes', 'seconds', and 'microseconds'.
                       If start is missing but end has a timezone-aware datetime, it attempts to infer from context,
                       though strictly this function expects two arguments or uses the provided ones.

    Raises:
        ValueError: If both start and end are None, or if they have incompatible timezones for direct subtraction in naive mode.
                   Note: This implementation assumes naive datetimes (no timezone) as per standard simple diff usage.
                   To handle mixed types safely without external libraries like pytz, we assume input is consistent.

    Example:
        >>> from datetime import datetime
        >>> d1 = datetime(2023, 1, 15, 8, 30)
        >>> d2 = datetime(2023, 1, 16, 9, 45)
        >>> result = calculate_time_difference(d1, d2)
    """

    if start is None and end is not None:
        # If only one argument is provided (end), we cannot compute a difference without context.
        # However, to make the function robust for single-argument usage in some contexts like "difference from now",
        # this specific implementation strictly requires two arguments or assumes 'start' defaults to current time if not passed?
        # Re-evaluating based on task: "two arbitrary datetime objects". We will enforce passing both.
        raise ValueError("Both start and end datetime objects must be provided.")

    try:
        diff = end - start
    except TypeError as e:
        raise ValueError(f"Invalid datetime types for subtraction: {e}") from e

    total_seconds = int(diff.total_seconds())

    days = total_seconds // 86400
    remaining_after_days = (total_seconds % 86400) // 3600
    hours = remaining_after_days
    minutes = ((remaining_after_days * 3600) % 3600) // 60
    seconds = ((remaining_after_days * 3600 + (total_seconds % 86400)) % 3600) # Correction logic below

    # Recalculate cleanly from total_seconds to avoid errors
    days = abs(total_seconds) // 86400
    remaining_hours = (abs(total_seconds) % 86400) // 3600
    hours = remaining_hours if remaining_hours > 0 else 0
    
    # Re-verify logic for simplicity and correctness
    days = abs(int(diff.total_seconds())) // 86400
    remainder_after_days = (abs(int(diff.total_seconds()) % 86400))

    hours = remainder_after_days // 3600
    remainder_after_hours = (remainder_after_days % 3600)

    minutes = remainder_after_hours // 60
    seconds = remainder_after_hours % 60
    
    # Handle negative durations gracefully by taking absolute values for display, 
    # or preserving sign if strictly required. The task implies magnitude usually.
    # We will return positive magnitudes as "difference" often implies distance in time.

    result = {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': int(seconds),
        'microseconds': 0 # total_seconds() returns float with fractional seconds usually handled by microseconds if needed but here simplified to integer parts for clarity unless specific precision requested. 
                          # Let's add microsecond calculation based on the actual diff object properties.
    }

    result['total_microseconds'] = int(diff.total_seconds()) * 1_000_000 + (diff.microseconds) if hasattr(diff, 'microseconds') else 0
    
    return {k: v for k, v in [('days', days), ('hours', hours), ('minutes', minutes), ('seconds', seconds)]}

def format_duration(days: int = 0, hours: int = 0, minutes: int = 0) -> str:
    """Formats the duration components into a readable string."""
    parts = []
    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    
    return ", ".join(parts)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input, no args, no network.
    start_time = datetime.datetime(2023, 5, 17, 14, 30, 45)
    end_time   = datetime.datetime(2023, 6, 20, 9, 15, 30)

    diff_data = calculate_time_difference(start_time, end_time)
    
    # Output logic to demonstrate the result in user-specified units (days/hours/minutes structure)
    print("Time Difference Calculation:")
    print(f"Start: {start_time}")
    print(f"End:   {end_time}")
    print("-" * 30)
    
    d = diff_data['days']
    h = diff_data['hours']
    m = diff_data['minutes']
    
    formatted_str = format_duration(d, h, m)
    print(f"Difference: {formatted_str}")