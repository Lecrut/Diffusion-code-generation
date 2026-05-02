from datetime import datetime
import pytz
def calculate_time_difference(tz_str1, tz_str2):
    tz1 = pytz.timezone(tz_str1)
    tz2 = pytz.timezone(tz_str2)
    offset1 = tz1.utcoffset(datetime.utcnow())
    offset2 = tz2.utcoffset(datetime.utcnow())
    if offset1 is None or offset2 is None:
        raise ValueError("Could not determine time zone offsets.")
    diff_seconds = abs(offset1.total_seconds() - offset2.total_seconds())
    diff_hours = diff_seconds / 3600.0
    return diff_hours
if __name__ == '__main__':
    tz1_config = "America/New_York"
    tz2_config = "Europe/London"
    try:
        difference = calculate_time_difference(tz1_config, tz2_config)
        print(difference)
    except pytz.exceptions.UnknownTimeZoneError as e:
        print(f"Error: One of the time zones is invalid. {e}")
    except ValueError as e:
        print(f"Error: {e}")