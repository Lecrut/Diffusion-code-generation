import datetime
from pytz import timezone

def convert_timezone(dt: datetime.datetime, target_tz_str: str) -> datetime.datetime:
    """
    Converts a given datetime object to the specified target time zone using pytz.
    
    Args:
        dt (datetime.datetime): The original datetime object without timezone info or with one to be converted.
        target_tz_str (str): A string representing the IANA time zone name (e.g., 'America/New_York').

    Returns:
        datetime.datetime: The new datetime object adjusted for the target time zone.
    
    Raises:
        ValueError: If the provided timezone string is not recognized by pytz.
    """

if __name__ == '__main__':
    pass
