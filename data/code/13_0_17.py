import pytz
from datetime import datetime

def calculate_time_difference(start_dt: datetime, end_dt: datetime) -> float:
    """
    Calculates the time difference in seconds between two naive datetime objects.
    
    Since 'pytz' is used to handle timezone-aware datetimes but requires conversion 
    for simple arithmetic on naive ones (or explicit zone handling), this function 
    assumes input datetimes are naive or have been converted to UTC before calling 
    if they were originally aware. However, strictly following the prompt's request 
    to use 'pytz' correctly with time zones:
    
    This implementation converts any timezone-aware inputs to a common reference (UTC) 
    using pytz for accurate calculation across different timezones. If naive datetimes 
    are provided without explicit zone info, they are treated as local system time, 
    but the robust usage pattern involves converting them via pytz after assigning an offset.
    
    Note: To strictly adhere to 'pytz' best practices which often require timezone-aware objects,
    this function converts naive datetimes by attaching a UTC tzinfo (as is common when 
    input zones are not specified) or handles explicit zone conversion if the inputs were 
    originally aware but passed in differently. For maximum correctness with pytz:
    
    1. If start_dt and end_dt have timezone info, convert both to UTC using their respective tzs.
    2. Subtract them to get a timedelta.
    3. Return total seconds from the resulting duration.

    Args:
        start_dt (datetime): The starting datetime object (naive or aware).
        end_dt (datetime): The ending datetime object (naive or aware).

    Returns:
        float: Time difference in seconds between end_dt and start_dt.
    
    Raises:
        ValueError: If inputs are not valid datetime objects.
    """
    if not isinstance(start_dt, datetime) or not isinstance(end_dt, datetime):
        raise ValueError("Both arguments must be datetime objects.")

    # Ensure both datetimes are timezone-aware using pytz for correct zone handling.
    # If naive, we treat them as UTC to ensure consistent calculation across zones 
    # without external context (as per the constraint of no interactive prompts/files).
    
    if start_dt.tzinfo is None:
        start_tz = pytz.UTC
        start_aware = start_dt.replace(tzinfo=start_tz)
    else:
        # If already aware, ensure it's in UTC for consistent subtraction 
        # (pytz handles conversion from other zones to local/UTC correctly).
        try:
            if hasattr(start_dt.tzinfo, 'localize'):
                # Some naive datetimes passed here might need localization first if they weren't converted yet.
                # But since we check tzinfo is None above for that case, this handles already aware zones.
                start_aware = start_dt.astimezone(pytz.UTC)
            else:
                start_aware = start_dt.astimezone(pytz.UTC)
        except Exception as e:
            # Fallback if astimezone fails on a weird tzinfo object, treat as UTC
            start_tz = pytz.UTC
            start_aware = start_dt.replace(tzinfo=start_tz)

    if end_dt.tzinfo is None:
        end_tz = pytz.UTC
        end_aware = end_dt.replace(tzinfo=end_tz)
    else:
        try:
            if hasattr(end_dt.tzinfo, 'localize'):
                # Similar logic for the second datetime to ensure it's in UTC.
                pass 
            end_aware = end_dt.astimezone(pytz.UTC)
        except Exception as e:
            end_tz = pytz.UTC
            end_aware = end_dt.replace(tzinfo=end_tz)

    # Calculate the difference using standard datetime subtraction on UTC objects.
    time_diff_seconds = (end_aware - start_aware).total_seconds()
    
    return time_diff_seconds

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or network access.
    
    # Sample 1: Two naive datetimes treated as UTC for consistent calculation across zones.
    dt_naive_1 = datetime(2023, 5, 17, 14, 0)
    dt_naive_2 = datetime(2023, 5, 18, 9, 30)
    
    # Sample 2: Timezone-aware datetimes in different zones (using pytz).
    tz_tokyo = pytz.timezone('Asia/Tokyo')
    utc_tz = pytz.UTC
    
    dt_aware_tokyo = datetime(2023, 5, 17, 14, 0)
    # Convert naive to aware in Tokyo time for demonstration of zone handling.
    dt_aware_tokyo_fixed = tz_tokyo.localize(dt_naive_1).replace(tzinfo=tz_tokyo)
    
    dt_aware_utc = datetime(2023, 5, 18, 9, 30)
    # Convert naive to aware in UTC.
    dt_aware_utc_fixed = utc_tz.localize(dt_naive_2).replace(tzinfo=utc_tz)

    result_seconds = calculate_time_difference(dt_aware_tokyo_fixed, dt_aware_utc_fixed)
    
    print(f"Time difference between Tokyo and UTC samples: {result_seconds} seconds")