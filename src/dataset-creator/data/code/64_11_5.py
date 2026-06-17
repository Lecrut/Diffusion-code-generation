import datetime
from zoneinfo import ZoneInfo
def format_localized_date(date_obj: datetime.datetime) -> str:
    try:
        tz = date_obj.tzinfo or ZoneInfo("UTC")
        formatted = date_obj.strftime("%Y-%m-%d") + " " + date_obj.strftime("%A, %B %d, %Y at %I:%M%p Z")
        return formatted
    except Exception:
        tz = ZoneInfo("UTC")
        dt_utc = date_obj.astimezone(tz)
        return f"{dt_utc.strftime('%Y-%m-%d')} {dt_utc.strftime('%A, %B %d, %Y at %I:%M%p UTC')}"
if __name__ == '__main__':
    samples = [
        datetime.datetime(2023, 10, 5, 14, 30),                                             
        datetime.datetime(2023, 10, 5, 14, 30, tzinfo=datetime.timezone.utc),        
        datetime.datetime.now(datetime.timezone.utc).replace(year=2024, month=12, day=25),                     
    ]
    for sample_date in samples:
        print(format_localized_date(sample_date))