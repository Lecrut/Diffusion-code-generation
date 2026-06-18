import pytz
from datetime import datetime

def convert_timezone(dt: datetime, target_tz_name: str) -> datetime:
    """
    Converts a given datetime object to the specified target timezone using pytz.
    
    Args:
        dt (datetime): The original datetime object in UTC or any existing local time.
        target_tz_name (str): Name of the target timezone string supported by pytz 
                              (e.g., 'America/New_York', 'Europe/London').

    Returns:
        datetime: A new datetime object representing the same instant in the target timezone.
    
    Raises:
        ValueError: If the provided timezone name is not recognized by pytz.
    """
    try:
        # Localize the input datetime to UTC if it hasn't been localized yet, 
        # or use the existing tzinfo and convert via a reference zone for accuracy.
        target_tz = pytz.timezone(target_tz_name)
        
        # If dt has no timezone info (naive), localize it as UTC first to ensure accuracy
        if dt.tzinfo is None:
            dt_utc = pytz.utc.localize(dt)
            converted_dt = dt_utc.astimezone(target_tz)
        else:
            # Convert from existing tz to target tz using the reference method for precision
            converted_dt = dt.astimezone(target_tz)
        
        return converted_dt

    except pytz.UnknownTimeZoneError as e:
        raise ValueError(f"Unsupported timezone name '{target_tz_name}'. Supported timezones must be recognized by pytz.") from e

if __name__ == '__main__':
    # Sample values - no user input, network access, or file dependencies required.
    
    # Example 1: Converting a naive datetime (assumed UTC) to America/New_York
    sample_naive = datetime(2023, 5, 15, 14, 30, 0)
    converted_naive = convert_timezone(sample_naive, 'America/New_York')

    # Example 2: Converting a UTC-aware datetime to Europe/London
    sample_utc_aware = datetime(2023, 6, 15, 14, 30, 0, tzinfo=pytz.utc)
    converted_utc = convert_timezone(sample_utc_aware, 'Europe/London')

    # Example 3: Converting a naive datetime to Asia/Tokyo (demonstrating daylight saving logic if applicable in the target zone)
    sample_naive_japan_time = datetime(2024, 1, 15, 9, 0, 0)
    converted_tokyo = convert_timezone(sample_naive_japan_time, 'Asia/Tokyo')

    print(f"Original Naive (assumed UTC): {sample_naive}")
    print(f"Converted to America/New_York: {converted_naive}")
    
    print("\n")
    
    print(f"Original UTC Aware: {sample_utc_aware}")
    print(f"Converted to Europe/London: {converted_utc}")
    
    print("\n")
    
    print(f"Original Naive (assumed UTC): {sample_naive_japan_time}")
    print(f"Converted to Asia/Tokyo: {converted_tokyo}")