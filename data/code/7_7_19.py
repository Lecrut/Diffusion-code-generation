import pytz
from datetime import datetime

def convert_timezone(dt: datetime, target_tz_name: str) -> datetime:
    """
    Converts a given datetime object to the specified target time zone using pytz.
    
    Parameters:
        dt (datetime): The original datetime object in UTC or any timezone.
        target_tz_name (str): Name of the target time zone (e.g., 'America/New_York').
        
    Returns:
        datetime: A new datetime object converted to the specified time zone.
    
    Raises:
        ValueError: If the provided time zone name is invalid or not found in pytz database.
    """
    try:
        target_tz = pytz.timezone(target_tz_name)
    except pytz.UnknownTimeZoneError as e:
        raise ValueError(f"Invalid timezone '{target_tz_name}'. Please check your input.") from e
    
    # If the datetime is naive, assume it's in UTC before converting to the target tz.
    if dt.tzinfo is None:
        utc = pytz.UTC
        converted_dt = utc.localize(dt)
    else:
        # Convert existing timezone-aware datetime to UTC first for consistency
        converted_dt = dt.astimezone(pytz.UTC).replace(tzinfo=utc)

    return target_tz.localize(converted_dt.replace(tzinfo=None))

if __name__ == '__main__':
    # Sample values - no user input, network access, or file dependencies required.
    
    # Example 1: Naive datetime (assumed UTC by default in this function)
    naive_datetime = datetime(2023, 6, 15, 14, 30, 0)
    
    # Example 2: Timezone-aware datetime in UTC
    utc_datetime = datetime(2023, 6, 15, 14, 30, 0, tzinfo=pytz.UTC)

    target_tz_name = 'America/New_York'
    
    result_naive = convert_timezone(naive_datetime, target_tz_name)
    result_aware = convert_timezone(utc_datetime, target_tz_name)
    
    print(f"Original Naive Datetime: {naive_datetime}")
    print(f"Converted to {target_tz_name}: {result_naive}")
    print("-" * 40)
    print(f"Original UTC Datetime: {utc_datetime}")
    print(f"Converted to {target_tz_name}: {result_aware}")