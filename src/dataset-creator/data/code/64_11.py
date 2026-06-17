import datetime
from zoneinfo import ZoneInfo
def format_localized_date(date_obj: datetime.datetime) -> str:
    try:
        return date_obj.astimezone(ZoneInfo("America/New_York")).strftime("%B %d, %Y")
    except Exception as e:
        raise ValueError(f"Failed to format timezone-aware datetime: {e}")
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5, 14, 30)
    print(format_localized_date(sample_date))