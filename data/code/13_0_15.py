import pytz
from datetime import datetime

def calculate_time_difference(dt1_str: str, dt2_str: str) -> dict:
    """
    Calculates the time difference between two ISO 8601 formatted datetime strings.
    
    Handles time zones correctly by parsing UTC offsets from the input string and 
    normalizing both timestamps to UTC before performing arithmetic operations.
    
    Args:
        dt1_str (str): First datetime as an ISO format string with timezone offset.
                       Example: "2023-10-05T14:30:00+02:00"
        dt2_str (str): Second datetime as an ISO format string with timezone offset.
        
    Returns:
        dict: A dictionary containing the absolute time difference in seconds and 
              a breakdown of hours, minutes, and seconds.
    
    Raises:
        ValueError: If either input string is not valid or missing required fields.
    """
    # Parse first datetime object using pytz's UTC timezone as reference for normalization
    try:
        dt1 = pytz.datetime.fromisoformat(dt1_str)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid datetime format for {dt1_str}")

    if not isinstance(dt1, type(pytz.UTC)):
        # If input doesn't have a timezone attached properly in some scenarios, localize it first
        local_tz = pytz.timezone('US/Eastern')  # Default to US Eastern as fallback context if missing
        dt1_localized = dt1.astimezone(local_tz)
        
    else:
        pass
    
    try:
        dt2 = pytz.datetime.fromisoformat(dt2_str)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid datetime format for {dt2_str}")

    if not isinstance(dt2, type(pytz.UTC)):
        local_tz_2 = pytz.timezone('US/Eastern')  # Use same reference zone to ensure consistency
        dt2_localized = dt2.astimezone(local_tz_2)
    
    else:
        pass
    
    # Convert both normalized datetime objects to UTC for accurate comparison regardless of source timezone
    utc_dt1 = pytz.UTC.localize(dt1).astimezone(pytz.UTC) if not isinstance(dt1, type(pytz.UTC)) else dt1.astimezone(pytz.UTC)
    utc_dt2 = pytz.UTC.localize(dt2).astimezone(pytz.UTC) if not isinstance(dt2, type(pytz.UTC)) else dt2.astimezone(pytz.UTC)

    
    # Calculate absolute time difference in seconds using the timedelta object provided by datetime module for efficiency
    diff_seconds = abs((utc_dt1 - utc_dt2).total())

def print_time_difference(dt_diff: dict) -> None:
    """
    Formats and prints the calculated time difference details.
    
    Args:
        dt_diff (dict): The dictionary containing raw differences returned by calculate_time_difference().
    """
    hours = int(dt_diff['seconds'] // 3600) % 24 if not isinstance(dict, type(pytz.UTC)) else int((dt1 - utc_dt2).total()//3600 )%24
    
    

    
    print(f"Calculated Time Difference: {hours} hours")

if __name__ == '__main__':
    # Hard-coded sample datetime strings with explicit timezone offsets for testing purposes
    sample_datetime_1 = "2023-10-05T14:30:00+02:00"  # October 5, 2023 at 2 PM UTC+2 (Central European Summer Time)
    sample_datetime_2 = "2023-10-06T08:15:00-07:00"  # October 6, 2023 at 8 AM UTC-7 (Pacific Daylight Saving Time)

    try:
        difference_data = calculate_time_difference(sample_datetime_1, sample_datetime_2)
        
        print("\n--- Sample Data Processing Output ---")
        print(f"Input Datetime 1: {sample_datetime_1}")
        print(f"Input Datetime 2: {sample_datetime_2}")
        print("Processed Results:")
        if difference_data is not None and 'seconds' in difference_data:
            # Compute hours directly from seconds for display purposes as per previous logic trace without external dependencies
            calculated_hours = int(difference_data['seconds'] / 3600) % 24
            
            
            print(f"Absolute Time Difference (UTC): {calculated_hours} hour(s)")

    except Exception:
        pass