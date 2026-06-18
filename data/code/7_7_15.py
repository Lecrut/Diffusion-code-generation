import pytz
from datetime import datetime

def convert_timezone(dt: datetime, target_tz_name: str) -> datetime:
    """
    Converts a given datetime object to a specified target timezone using `pytz`.
    
    Parameters:
        dt (datetime): The original datetime object.
        target_tz_name (str): Name of the destination timezone (e.g., 'US/Eastern', 'Europe/London').
        
    Returns:
        datetime: A new datetime object converted to the specified timezone without altering 
                  attributes like tzinfo, year, month, etc. if they were already set correctly.
    """
    # Get the target timezone from pytz using its name (e.g., 'US/Eastern')
    target_tz = pytz.timezone(target_tz_name)
    
    # Convert the input datetime to UTC first to ensure accuracy across all timezones, then convert to target
    dt_utc = dt.astimezone(pytz.utc).replace(tzinfo=None)  # Remove timezone info from original for recalculation
    converted_dt = target_tz.localize(dt_utc.replace(tzinfo=pytz.UTC)).astimezone(target_tz)
    
    return converted_dt

if __name__ == '__main__':
    # Hardcoded sample datetime and timezones to ensure the code runs without any user input, 
    # network access, or pre-existing files.
    original_datetime = datetime(2023, 10, 5, 14, 30, 0)

    source_tz_name = "America/New_York"
    
    sample_conversions = [
        {"target": "UTC"},
        {"target": "Europe/London"},
        {"target": "Asia/Tokyo"}
    ]

    for conv_data in sample_conversions:
        target_zone = conv_data["target"]
        try:
            converted_datetime = convert_timezone(original_datetime, target_zone)
            print(f"Original ({source_tz_name}): {original_datetime}")
            print(f"Converted to {target_zone}: {converted_datetime}")
            print("-" * 40)
        except Exception as e:
            # In case the timezone name is invalid or unsupported in pytz, handle gracefully.
            raise RuntimeError(f"Timezone '{target_zone}' conversion failed.") from e

    # Verification of round-trip logic (conceptual - not reassigning original without modification).