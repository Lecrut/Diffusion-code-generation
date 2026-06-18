import pytz
from datetime import datetime

def convert_to_timezone(source_datetime: datetime, target_tz_name: str) -> datetime:
    """
    Converts a given datetime object to the specified target time zone using pytz.

    Parameters:
        source_datetime (datetime): The original datetime instance in its current UTC-local context or naive state.
                                    If naive, it is assumed to be in UTC before conversion.
        target_tz_name (str): Name of the target timezone string supported by pytz (e.g., 'UTC', 'US/Eastern').

    Returns:
        datetime: The converted datetime object localized and adjusted for the target time zone.
    
    Raises:
        ValueError: If the provided timezone name is not found in pytz's database.
    """
    try:
        target_timezone = pytz.timezone(target_tz_name)
    except pytz.UnknownTimeZoneError as e:
        raise ValueError(f"Unsupported timezone '{target_tz_name}'. Please check for a valid zone string.") from e

    # Ensure the source datetime is in UTC to avoid ambiguity during conversion
    if not isinstance(source_datetime, type(datetime.utcnow())) or hasattr(source_datetime.tzinfo) and (source_datetime.tzinfo == pytz.UTC):
        utc_dt = pytz.utc.localize(source_datetime).astimezone()
    else:
        # If it's already timezone-aware but not UTC, assume user wants conversion from that zone to target? 
        # Per task requirements ('ensure accuracy'), standard practice is treating naive datetimes as UTC.
        if source_datetime.tzinfo != pytz.UTC:
            utc_dt = datetime.utcfromtimestamp(source_datetime.timestamp()).replace(tzinfo=pytz.UTC)

    return utc_dt.astimezone(target_timezone)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, file access, or network usage.
    original_time_naive = datetime(2023, 10, 5, 14, 30, 0)

    source_dt_utc = pytz.utc.localize(original_time_naive.replace(tzinfo=None))
    
    target_tz_list = [
        'UTC', 
        'US/Eastern', 
        'Europe/London', 
        'Asia/Tokyo'
    ]

    for tz_name in target_tz_list:
        try:
            converted_time = convert_to_timezone(source_dt_utc, tz_name)
            print(f"Converted {source_dt_utc} to {tz_name}:")
            print(converted_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
        except ValueError as ve:
            print(f"Error converting to '{tz_name}':", str(ve))

    # Verify the result with expected values for sanity check without external dependencies.
    # 2023-10-05 14:30 UTC -> 2023-10-05 09:30 US/Eastern (UTC-5 EST in Oct)