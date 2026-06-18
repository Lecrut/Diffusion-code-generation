import pytz
from datetime import datetime

def convert_to_timezone(dt: datetime, target_tz_name: str) -> datetime:
    """
    Converts a given datetime object to the specified target timezone using pytz.
    
    Parameters:
        dt (datetime): The original datetime object without timezone info or with one to be converted.
        target_tz_name (str): Name of the target timezone as recognized by IANA DB (e.g., 'UTC', 'America/New_York').
        
    Returns:
        datetime: A new datetime instance adjusted to the target timezone.
    
    Raises:
        ValueError: If the provided timezone name is invalid or already has incorrect info causing ambiguity.
    """
    try:
        # Get the target timezone object from pytz
        target_tz = pytz.timezone(target_tz_name)
        
        # Handle naive datetime (no tzinfo)
        if dt.tzinfo is None:
            # Attach UTC to a naive datetime for consistent conversion
            aware_dt = pytz.UTC.localize(dt)
        else:
            # If it's already timezone-aware, convert directly via localize() logic or replace_tzinfo
            # Note: For existing timezones that are not UTC, we should normalize the input first if needed. 
            # However, for simple conversion assuming correct start with pytz:
            
            aware_dt = dt
        
        # Perform the conversion to target timezone
        converted_datetime = target_tz.localize(aware_dt)
        
        return converted_datetime

    except Exception as e:
        raise ValueError(f"Error converting time zone: {str(e)}")

if __name__ == '__main__':
    # Sample datetime without timezone (naive), assumed to be in a generic context or UTC if not specified explicitly.
    sample_naive = datetime(2023, 10, 5, 14, 30, 0)

    target_timezone_name = "America/New_York"

    converted_datetime = convert_to_timezone(sample_naive, target_timezone_name)

    print(f"Original (naive): {sample_naive}")
    print(f"Converted to {target_timezone_name}: {converted_datetime}")