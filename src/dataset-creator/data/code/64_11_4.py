import datetime
from zoneinfo import ZoneInfo as get_timezone
def format_localized_date(date_obj: datetime.datetime) -> str:
    if not isinstance(date_obj, datetime.datetime):
        raise TypeError("Input must be a datetime object.")
    try:
        tz = get_timezone(date_obj.tzname())
    except Exception:
        return date_obj.strftime("%B %d, %Y")
    formatted_date = date_obj.astimezone(tz).strftime("%A, %B %d, %Y at %I:%M %p in %Z (%Z)")
    return formatted_date
if __name__ == '__main__':
    sample_dates = [
        datetime.datetime(2023, 10, 5, 14, 30),
        datetime.datetime(2024, 6, 18, 9, 15, tzinfo=datetime.timezone(datetime.timedelta(hours=5))),
    ]
    for date in sample_dates:
        print(format_localized_date(date))