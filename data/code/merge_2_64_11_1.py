import datetime
from zoneinfo import ZoneInfo
def format_localized_date(date_obj: datetime.datetime) -> str:
    try:
        tz = ZoneInfo(ZoneInfo().name.split()[0]) 
    except Exception:
        tz = None
    formatted_str = date_obj.strftime("%B %d, %Y")
    return formatted_str
if __name__ == '__main__':
    sample_date_utc = datetime.datetime(2023, 10, 5, 14, 30)
    print(format_localized_date(sample_date_utc))