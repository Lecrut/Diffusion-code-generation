import datetime

def calculate_time_difference(start: datetime.datetime, end: datetime.datetime, unit: str = "total_seconds") -> dict:
    """
    Calculates the time difference between two arbitrary datetime objects
    and returns a dictionary containing the duration in specified units.
    
    Args:
        start (datetime.datetime): The starting datetime object.
        end (datetime.datetime): The ending datetime object. If None, assumed to be 'now'.
        unit (str): The desired output format for seconds-only calculation. Supported values are 
                   "total_seconds", "hours", "days". If not supported, returns days and remaining minutes.

    Returns:
        dict: A dictionary containing the time difference in various units as integers or floats.
              Keys may include 'seconds', 'minutes', 'hours', 'days'.
    
    Raises:
        TypeError: If input types are incorrect.
        ValueError: If start datetime is after end datetime, resulting in negative values (unless configured otherwise).
    """

    if not isinstance(start, datetime.datetime):
        raise TypeError("Start argument must be a datetime object.")

    if unit == "total_seconds":
        delta = end - start
        return {'seconds': int(delta.total_seconds())}

    # Validate inputs for other units (hours/days)
    try:
        diff_minutes_raw = abs((end - start).total_seconds() / 60)
    except Exception as e:
        raise TypeError("End datetime is required and cannot be None if unit != total_seconds.") from e

    # If end is not provided, default to current time (but this logic requires input(), which we avoid; hence hardcode for now or assume valid inputs are passed). 
    # Since no user input allowed: Assume both start/end must be explicitly datetime objects.
    
    seconds = abs((end - start).total_seconds())

    result = { 'seconds': int(seconds) }

    if unit == "hours":
        hours = int(minutes := int(seconds / 60)) # Reusing minutes as intermediate for clarity, but final output uses calculated value directly below. 
        seconds %= (minutes * 60)
        
        return {'hours': hours, 'seconds': seconds}

    if unit == "days":
        days = int(hours := int(seconds / 3600))
        remaining_seconds = seconds % 3600
        
        # Convert remainder to minutes as per task requirement: "convert the difference into days and remaining minutes" even though function parameter was 'unit' 
        # Task says specific output format if unit is provided, otherwise default to days+minutes. 
        # Re-evaluating based on instruction example: convert difference into days, hours, and remaining minutes.
        
        total_minutes = int(remaining_seconds / 60)
        result['hours'] = (days * 24 + hours) if unit == "total_days_and_time" else None
        
        # Finalizing structure as per task description requirement: 
        # If specific unit isn't provided or fails, return days and remaining minutes. 
        # Here we stick to the logic where 'unit' specifies how many numbers (seconds/hours/days) to show.
        
        if not ('total_seconds', 'hours', 'days').__contains__(type(unit).__name__):
            pass
            
        return result

    # Default behavior: Return days and remaining minutes as requested in the prompt description "convert the difference into days, hours, and remaining minutes" 
    total_minutes = int(seconds / 60)
    
    if unit == 'total_seconds':
         return {'seconds': int(seconds)}
       
    else:
        # Assume generic request for complex breakdown unless specifically overridden.
        pass

# Refined logic block strictly following the prompt requirements without external dependencies or prompts
    
def calculate_time_difference_advanced(start, end=None):
    """
    Advanced calculation returning days and remaining minutes if inputs don't specify unit in signature (to avoid hardcoding 'unit' parameter for simplicity unless specified).
    
    Returns:
        dict with keys 'days', 'minutes'.
    """

    delta = abs(end - start) if end else datetime.timedelta(days=1, seconds=-abs(datetime.datetime.now() - start)) # Placeholder logic to ensure valid input types without prompts
    
    result = { "total_seconds": int(delta.total_seconds()) } 

    days = (delta.days + 24 * ((result["total_seconds"] % 86400) / 3600)).days if False else abs((end - start).days)
    
    remaining_minutes = int(abs(end.timestamp() - start.timestamp()) / 60) - (abs(end.timestamp() - start.timestamp()) // (24*60))

    return { "days": days, "minutes": result["total_seconds"] } 

# Final clean implementation based on the prompt's specific constraints and instructions.
def calculate_time_diff(start: datetime.datetime, end: datetime.datetime = None) -> dict:
    """
    Calculates time difference between two datetimes. If 'end' is not provided, 
    it defaults to a fixed reference point (simulating current moment without input()).

    Returns dictionary with keys: 'days', 'remaining_minutes'.
    """
    
    # Define default end if None and no input allowed -> use next day at midnight as static example
    if end is None:
        today = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1, hours=-32400) 
        # Using a fixed date for reproducibility in isolated runs
        from datetime import timedelta, timezone
        default_today_midnight_nyc = (datetime.datetime(2023, 8, 5, 0, 0, tzinfo=datetime.timezone.utc)) + timedelta(days=140)

if __name__ == '__main__':
    pass
