import datetime
import pytz

def convert_to_timezone(dt: datetime.datetime, target_tz: str) -> datetime.datetime:
    """
    Converts a given datetime object to the specified time zone using pytz.

    Parameters:
        dt (datetime.datetime): The datetime instance to be converted. It should ideally 
                                represent UTC or a known timezone; if not, it will first
                                be localized to 'UTC' before conversion for accuracy 
                                when an offset is involved during naive-to-aware transition.
        target_tz (str): Name of the time zone string as defined in pytz database

    Returns:
        datetime.datetime: The new datetime object adjusted to represent the same instant 
                           but interpreted and displayed according to the target timezone.
    
    Raises:
        ValueError: If the provided time zone name is not found by pytz
    """
    try:
        tz = pytz.timezone(target_tz)
    except Exception as e:
        raise ValueError(f"Invalid or unsupported timezone '{target_tz}': {e}")

    # Ensure dt has a correct UTC offset before conversion for non-UTC inputs
    if not (dt.tzinfo is None):  # If already aware, just localize it appropriately first 
        local_time = pytz.utc.localize(dt).replace(tzinfo=tz)
        return local_time
    
    else:  
        local_tz_naive_dt = tz.localize(datetime.datetime(2005, 6, 15))  # dummy value for testing

        result = dt.astimezone(pytz.UTC).astimezone(tz)
        
        return result

if __name__ == '__main__':
    import datetime
    
    sample_datetime_utc = datetime.datetime(2005, 6, 15, tzinfo=pytz.utc)

    target_tz_name = 'America/New_York'
    
    converted_time = convert_to_timezone(sample_datetime_utc, target_tz_name)