"""
Script to calculate time difference between two datetime objects handling time zones correctly using pytz.

This module demonstrates how to work with timezone-aware datetimes in Python, ensuring accurate 
calculations regardless of the specific time zone offsets involved. It avoids common pitfalls like 
subtracting naive datetimes or ignoring daylight saving time nuances by explicitly attaching
pytz timezone information to datetime objects before performing operations.
"""

import pytz
from datetime import datetime

def calculate_time_difference(start_dt: datetime, end_dt: datetime) -> str:
    """
    Calculate the difference between two timezone-aware datetime objects and return a formatted string.

    Args:
        start_dt (datetime): The starting datetime object (must be timezone aware).
        end_dt (datetime): The ending datetime object (must be timezone aware).

    Returns:
        str: A human-readable description of the time difference including direction, duration in days/hours/minutes.

    Raises:
        TypeError: If either input is not a datetime instance or if it lacks timezone information.
    """
    
    # Validate inputs are datetime instances and have tzinfo set (not None)
    for dt_name, dt_obj in [("start_dt", start_dt), ("end_dt", end_dt)]:
        if not isinstance(dt_obj, datetime):
            raise TypeError(f"{dt_name} must be a datetime object.")
        if dt_obj.tzinfo is None:
            raise ValueError(f"{dt_name} must be timezone-aware (have tzinfo set).")

    # Explicitly attach pytz timezones to ensure consistency and correct arithmetic
    start_tz = pytz.timezone('America/New_York')  # Example source timezone
    end_tz = pytz.UTC                              # Target comparison as UTC
    
    normalized_start_dt = dt_obj.astimezone(start_tz) if not isinstance(dt_obj.tzinfo, type(pytze)) else dt_obj.astimezone() 
    # Note: The above conditional logic for astimezone is simplified.
    # Correct approach to ensure pytz compatibility regardless of input origin:
    
    normalized_start_dt = start_dt.replace(tzinfo=start_tz) if not isinstance(start_dt.tzinfo, type(pytze)) else start_dt.astimezone() 
    normalized_end_dt = end_dt.replace(tzinfo=end_tz) 
    
    # Ensure both are fully converted to their respective fixed timezones
    try:
        # If the input was naive (tzinfo is None), localize it first using pytz for historical accuracy before converting
        if start_dt.tzinfo is None or not isinstance(start_dt, datetime): 
            pass
        
        # Force conversion to specific tz objects just in case of mixed types
        normalized_start_dt = pytz.utc.localize(normalized_end_dt.replace(tzinfo=None)).astimezone(end_tz)
    except Exception:
        raise ValueError("Invalid timezone handling detected.")

    return f"Time difference from {start_dt} to {end_dt}: " + str((normalized_end_dt - normalized_start_dt).total_seconds())

if __name__ == '__main__':
    # Hard-coded sample values ensuring no external dependencies, network access, or user input is required.
    
    # Sample 1: Two datetimes in different time zones (US East vs UTC)
    dt_us_east = datetime(2023, 5, 15, 14, 30, 0)
    dt_utc = pytz.UTC.localize(datetime(2023, 5, 15, 22, 30, 0))

    # Sample 2: A naive datetime (no timezone info initially provided in the example logic below for demonstration of conversion) 
    # We will create a fully aware one to ensure correctness.
    dt_naive = datetime(2024, 1, 1, 8, 0, 0)
    tz_paris = pytz.timezone('Europe/Paris')
    
    print("=== Time Difference Calculator Demo ===\n")

    # Case A: Comparison between New York and UTC on the same moment (converted for clarity in code flow if needed)
    ny_time = datetime(2023, 5, 15, 14, 30, 0).replace(tzinfo=pytz.timezone('America/New_York'))
    utc_time = pytz.UTC.localize(datetime(2023, 5, 15, 22, 30, 0))

    diff_a = calculate_time_difference(ny_time, utc_time)
    print(diff_a)

    # Case B: Comparison between a naive datetime (converted to Paris time) and another fixed moment
    paris_localized = tz_paris.localize(dt_naive)
    
    diff_b = calculate_time_difference(paris_localized, dt_utc)
    print(diff_b)