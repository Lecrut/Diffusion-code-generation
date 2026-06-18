import pytz
from datetime import datetime

def convert_timezone(dt: datetime, target_tz_name: str) -> datetime:
    """
    Converts a given datetime object to the specified target time zone using pytz.
    
    Args:
        dt (datetime): The original datetime object in UTC or any timezone.
        target_tz_name (str): Name of the target time zone string (e.g., 'America/New_York').

    Returns:
        datetime: A new datetime object converted to the specified time zone.
    
    Raises:
        ValueError: If the provided time zone name is invalid or not supported by pytz.
    """
    try:
        target_tz = pytz.timezone(target_tz_name)
    except pytz.UnknownTimeZoneError as e:
        raise ValueError(f"Invalid timezone specified: {target_tz_name}") from e

    # If the input datetime is naive, assume it's in UTC before converting.
    if dt.tzinfo is None:
        dt = pytz.utc.localize(dt)

    converted_dt = target_tz.localize(dt).astimezone(target_tz)
    
    return converted_dt

if __name__ == '__main__':
    # Sample datetime object in UTC (naive, assumed to be UTC for conversion logic demonstration)
    sample_datetime_utc = datetime(2023, 10, 5, 14, 30, 0)

    target_timezone_name = 'America/New_York'

    try:
        converted_result = convert_timezone(sample_datetime_utc, target_timezone_name)
        
        print(f"Original UTC Time (naive): {sample_datetime_utc}")
        print(f"Converted to {target_timezone_name}: {converted_result}")
    except ValueError as ve:
        print(f"Error during conversion: {ve}")