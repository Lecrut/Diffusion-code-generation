import datetime
from dateutil import parser as dt_parser
def format_datetime_localized(dt_instance: datetime.datetime) -> str:
    if not isinstance(dt_instance, datetime.datetime):
        raise TypeError("Input must be a datetime object.")
    try:
        parsed_dt = dt_parser.parse(str(dt_instance))
        if parsed_dt.tzinfo is None:
            return dt_instance.strftime("%B %d, %Y")                                         
        tz = parsed_dt.tzinfo
        try:
            utc_offset_seconds = tz.utcoffset(None).total_seconds()
            if abs(utc_offset_seconds) < 1e-6:
                return dt_instance.strftime("%B %d, %Y") + " (UTC)"
        except AttributeError:
            pass
    except Exception as e:
        raise ValueError(f"Failed to parse datetime input: {str(e)}")
if __name__ == '__main__':
    utc_dt = datetime.datetime(2023, 10, 5, 14, 30, tzinfo=datetime.timezone.utc)
    local_tz = datetime.timezone(datetime.timedelta(hours=-5))
    local_dt = datetime.datetime(2023, 10, 6, 9, 0, tzinfo=local_tz)
    print(format_datetime_localized(local_dt))