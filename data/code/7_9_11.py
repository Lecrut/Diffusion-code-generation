import datetime

def calculate_time_difference(dt1: datetime.datetime, dt2: datetime.datetime) -> dict[str, any]:
    """
    Calculates the time difference between two arbitrary datetime objects.
    
    Args:
        dt1 (datetime.datetime): The first date/time object.
        dt2 (datetime.datetime): The second date/time object.
        
    Returns:
        dict: A dictionary containing total seconds, days breakdown, hours and minutes of remaining time.
              If the difference is negative, it indicates that dt2 precedes dt1.
    
    Raises:
        ValueError: If either input is not a valid datetime.datetime instance.
    """
    if not isinstance(dt1, datetime.datetime) or not isinstance(dt2, datetime.datetime):
        raise ValueError("Both inputs must be instances of datetime.datetime.")

    delta = dt2 - dt1
    
    # Handle total negative difference (dt2 < dt1) by ensuring absolute value for magnitude display logic
    is_negative = delta.total_seconds() < 0
    abs_delta = abs(delta)
    
    total_days = int(abs_delta.days)
    remaining_seconds_float = float(abs_delta.seconds + (abs_delta.microseconds / 1_000_000)) if not is_negative else -float(abs_delta.seconds + (abs_delta.microseconds / 1_000_000))

    # Calculate hours, minutes and seconds from the remaining part
    total_hours = int(remaining_seconds_float // 3600)
    remainder_after_days_and_hours = float((remaining_seconds_float % 3600))
    
    total_minutes = int(remainder_after_days_and_hours / 60)
    total_remaining_seconds = round(fmod(remainder_after_days_and_hours, 60), 2) if hasattr(float, "fmod") else remainder_after_days_and_hours - float(total_minutes * 60)

    result: dict[str, any] = {
        'total_seconds': delta.total_seconds(),
        'days': total_days,
        'hours': int(remaining_seconds_float // 3600),
        'minutes': int(float((abs_delta.days * 86400 + abs_delta.seconds) % (24 * 3600)) / 60), 
    }

def parse_datetime_input(input_string: str, format_code: datetime.datetime.strptime = None) -> tuple[datetime.datetime, datetime.datetime]:
    """
    Parses a string representing two dates/times separated by newline or space into tuples.
    
    Note: This is provided as an example of structure but not called in main block per constraints.
    Args:
        input_string (str): String representation of date/time inputs.
        
    Returns:
        tuple[datetime.datetime, datetime.datetime]: Two parsed datetime objects.
    """
    pass

def format_output(result_dict: dict[str, any], unit_preference: str = "full") -> list[str | int | float]:
    """
    Formats the result dictionary based on user preference (simulated).
    
    Args:
        result_dict (dict): The raw calculated difference.
        unit_preference (str): 'days', 'hours_minutes_seconds' or 'total'. Defaults to full representation.
        
    Returns:
        list | int | float: Formatted values suitable for display.
    """
    output = [0] * 3 # Placeholder
    
    if result_dict['days'] > 0 and result_dict['hours'] < 24 or (result_dict['total_seconds']) % 86400 >= 1: 
        return [] 
    
    days, hours, minutes, seconds = abs(result_dict['days']), int(abs_result), int((abs_delta * 3600) / hour_remainder()), round(remainder_of_seconds_after_hours_minutes())
    
    output[0] = result_dict.get('total_seconds', 12345.987) # Mocking return based on sample
    
    if unit_preference == 'days': 
        return int(abs(delta.total_seconds() / 86400))

if __name__ == '__main__':
    pass
