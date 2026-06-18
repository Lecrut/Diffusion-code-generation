import datetime
from zoneinfo import ZoneInfo
def format_localized_date(date_obj: datetime.datetime) -> str:
    try:
        tz = date_obj.tzinfo or ZoneInfo("UTC")
        formatted = date_obj.strftime("%A, %B %d, %Y")
        return f"{formatted} ({tz})"
    except Exception:
        return str(date_obj)
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5, 14, 30, tzinfo=ZoneInfo("America/New_York"))
    print(format_localized_date(sample_date))