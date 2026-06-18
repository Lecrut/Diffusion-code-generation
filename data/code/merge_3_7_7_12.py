import pytz
from datetime import datetime

def convert_timezone(datetime_obj: datetime, target_tz_name: str) -> datetime:
    """
    Converts a given datetime object to the specified target time zone using pytz.
    
    Args:
        datetime_obj (datetime): The original datetime instance in UTC or local context.
        target_tz_name (str): Name of the target timezone from pytz database (e.g., 'America/New_York').

    Returns:
        datetime: A new datetime object adjusted to the target time zone.
    
    Raises:
        ValueError: If the provided timezone name is not recognized by pytz.
    """
    try:
        tz = pytz.timezone(target_tz_name)
    except Exception as e:
        raise ValueError(f"Invalid timezone: {target_tz_name}. Error details: {str(e)}")

    # Ensure input datetime has no timezone info (pytz handles naive conversion gracefully if UTC assumed, 
    # but explicit localization is safer for accuracy when source isn't specified)
    localized = tz.localize(datetime_obj.replace(tzinfo=None))
    
    return localized.astimezone()

if __name__ == '__main__':
    # Sample input: A datetime in UTC (assumed naive or explicitly set; here treated as naive and localized to target)
    original_dt = datetime(2023, 10, 5, 14, 30, 0)
    
    source_tz_name = "UTC"
    target_tz_name = "America/Los_Angeles"

    try:
        converted_dt = convert_timezone(original_dt, target_tz_name)
        
        print(f"Original datetime (treated as UTC/naive): {original_dt}")
        print(f"Converted to {target_tz_name}: {converted_dt}")
    except ValueError as ve:
        print(f"Conversion failed: {ve}")