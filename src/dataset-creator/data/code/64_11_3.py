import datetime
from zoneinfo import ZoneInfo
def format_localized_date(date_obj: datetime.datetime) -> str:
    try:
        tz = date_obj.tzinfo or ZoneInfo("UTC")
        formatted = date_obj.strftime("%B %d, %Y")
        return f"{formatted} {date_obj.tzname(date_obj)}"
    except Exception:
        if not date_obj.tzinfo:
            tz_name = "UTC"
        else:
            try:
                from zoneinfo import ZoneInfo
                tz_name = str(date_obj.astimezone(ZoneInfo("America/New_York")).tzname())
            except ImportError:
                return date_obj.strftime("%B %d, %Y")
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5, 14, 30)
    print(format_localized_date(sample_date))