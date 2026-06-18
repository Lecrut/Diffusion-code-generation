import datetime
from zoneinfo import ZoneInfo as get_timezone
def format_date(date_obj: datetime.datetime) -> str:
    if not isinstance(date_obj, datetime.datetime):
        raise TypeError("Input must be a datetime object")
    try:
        tz = date_obj.tzinfo or get_timezone('UTC')
        return date_obj.astimezone(tz).strftime('%B %d, %Y at %H:%M in {time_zone}')
    except Exception as e:
        raise RuntimeError(f"Date formatting failed due to timezone error") from e
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5, 14, 30)
    print(format_date(sample_date))